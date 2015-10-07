# Connor McLaughlin
#
# Simple spell checker that uses a slightly modified version of the Levenshtein distance

import sys

dict_file = open(sys.argv[1], 'r')
misspellings_file = open(sys.argv[2], 'r')
corrections_file = open('suggestions.txt', 'w')

dictionary = dict_file.read().split('\n')
dictionary.pop()
dict_file.close()

misspellings = misspellings_file.read().split('\n')
misspellings.pop()
misspellings_file.close()


def sub_cost(source_char, target_char):
    if source_char == target_char:
        return 0
    elif (source_char == 'a' and target_char == 'e') or (source_char == 'e' and target_char == 'a'):
        return 1  # see (ii)
    elif (source_char == 's' and target_char == 'c') or (source_char == 'c' and target_char == 's'):
        return 1  # see (iii)
    else:
        return 2


def ins_cost(first_or_last, char):
    return 1 if not first_or_last else 2  # see (i)


def del_cost(first_or_last, char):
    if first_or_last:
        return 4       # see (i) and (vi)
    elif char == 'c':  # see (iv)
        return 4
    elif char == 'v':  # see (v)
        return 4
    else:
        return 1


def min_distance(target, source):
    n = len(target)
    m = len(source)

    distance = [[0 for x in range(m+1)] for x in range(n+1)]

    # the weird boolean expressions in the cost functions tell if at the beginning/end of a word
    # see (i)
    for i in range(1, n+1):
        distance[i][0] = distance[i-1][0] + ins_cost(i == 1 or i == n + 1, target[i-1])

    for j in range(1, m+1):
        distance[0][j] = distance[0][j-1] + del_cost(j == 1 or j == m + 1, source[j-1])

    for i in range(1, n+1):
        for j in range(1, m+1):
            distance[i][j] = min(distance[i-1][j] + ins_cost(i == 1 or i == n + 1 or j == 1 or j == m + 1, target[i-1]), distance[i-1][j-1] + sub_cost(source[j-1], target[i-1]), distance[i][j-1] + del_cost(i == 1 or i == n + 1 or j == 1 or j == m + 1, source[j-1]))

    return distance[n][m]


for word in misspellings:
    abs_min = min_distance(dictionary[0], word)
    correction = dictionary[0]
    for target in dictionary[1:len(dictionary)]:
        new_min = min_distance(target, word)
        if new_min <= abs_min:
            abs_min = new_min
            correction = target

    corrections_file.write(correction+'\n')

corrections_file.close()

# Connor McLaughlin

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
    return 0 if source_char == target_char else 2


def ins_cost():
    return 1


def del_cost():
    return 1


def min_distance(target, source):
    n = len(target)
    m = len(source)

    distance = [[0 for x in range(m+1)] for x in range(n+1)]

    for i in range(1, n+1):
        distance[i][0] = distance[i-1][0] + ins_cost()

    for j in range(1, m+1):
        distance[0][j] = distance[0][j-1] + del_cost()

    for i in range(1, n+1):
        for j in range(1, m+1):
            distance[i][j] = min(distance[i-1][j] + ins_cost(), distance[i-1][j-1] + sub_cost(source[j-1], target[i-1]), distance[i][j-1] + del_cost())

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

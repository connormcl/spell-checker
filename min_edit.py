# Connor McLaughlin
#
# Script that computes the Levenshtein distance between two words

import sys

target = sys.argv[1]
source = sys.argv[2]

n = len(target)
m = len(source)

distance = [[0 for x in range(m+1)] for x in range(n+1)]


def sub_cost(source_char, target_char):
    return 0 if source_char == target_char else 2


def ins_cost():
    return 1


def del_cost():
    return 1

for i in range(1, n+1):
    distance[i][0] = distance[i-1][0] + ins_cost()

for j in range(1, m+1):
    distance[0][j] = distance[0][j-1] + del_cost()

for i in range(1, n+1):
    for j in range(1, m+1):
        distance[i][j] = min(distance[i-1][j] + ins_cost(), distance[i-1][j-1] + sub_cost(source[j-1], target[i-1]), distance[i][j-1] + del_cost())

# Uncomment this code to view the table being used
# for i in range(0, n+1):
#     print distance[i]

print distance[n][m]

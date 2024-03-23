# https://www.acmicpc.net/problem/3568

import sys

segments = sys.stdin.readline().split()

for i in range(1, len(segments)):
    segment = segments[i]

    suffix_idx = 1
    for j in range(len(segment)):
        if not segment[j].isalpha():
            suffix_idx = j
            break

    var_types = ''
    for j in range(len(segment) - 2, suffix_idx - 1, -1):
        if segment[j] == "]":
            var_types += "[]"
        elif segment[j] != "[":
            var_types += segment[j]
    
    print(segments[0] + var_types + ' ' + segment[:suffix_idx] + ';')




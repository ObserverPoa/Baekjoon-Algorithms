import sys

inputA_count = int(sys.stdin.readline())

A = set(map(int, sys.stdin.readline().split()))

inputM_count = int(sys.stdin.readline())

M = list(map(int, sys.stdin.readline().split()))

for m in M:
    if m in A:
        print(1)
    else:
        print(0)






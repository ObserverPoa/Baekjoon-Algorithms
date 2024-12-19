import sys

input = sys.stdin.readline

N = int(input())

upper_line = list(map(int, input().split()))
for _ in range(N - 1):
    line = list(map(int, input().split()))
    for i in range(len(line)):
        larger = float('-inf')
        if i > 0:
            larger = max(upper_line[i - 1], larger)
        if i < len(line) - 1:
            larger = max(upper_line[i], larger)
        line[i] += larger
    upper_line = line

print(max(upper_line))
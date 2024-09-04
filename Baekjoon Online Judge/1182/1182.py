import sys
import itertools

N, S = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

answer = 0

for size in range(1, N + 1):
    for sequence in itertools.combinations(numbers, size):
        if sum(sequence) == S:
            answer += 1

print(answer)
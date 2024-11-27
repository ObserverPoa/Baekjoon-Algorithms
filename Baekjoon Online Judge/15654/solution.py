import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def dfs(sequence):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for number in numbers:
        if number in sequence:
            continue

        sequence.append(number)
        dfs(sequence)
        sequence.pop()

dfs([])
import sys

N, M = map(int, sys.stdin.readline().split())

def dfs(num, sequence):
    if len(sequence) == M:
        print(' '.join(sequence))
        return
    
    for i in range(num, N):
        sequence.append(str(i + 1))
        dfs(i + 1, sequence)
        sequence.pop()

dfs(0, [])

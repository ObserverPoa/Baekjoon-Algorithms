import sys

input = sys.stdin.readline

N, P, Q = map(int, input().split())

memo = dict()

def sequence_A(i):
    if i == 0:
        return 1
    elif i in memo:
        return memo[i]
    
    ret = sequence_A(i // P) + sequence_A(i // Q)
    memo[i] = ret
    return ret

print(sequence_A(N))
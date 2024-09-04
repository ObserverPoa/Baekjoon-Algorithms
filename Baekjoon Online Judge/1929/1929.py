import sys

M, N = map(int, sys.stdin.readline().split())

is_prime = [True] * (N + 1)

for i in range(2, N + 1):
    if is_prime[i]:
        if i >= M:
            print(i)

        j = 2
        while i * j <= N:
            is_prime[i * j] = False
            j += 1
        

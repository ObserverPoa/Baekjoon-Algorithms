import sys

input = sys.stdin.readline

N = int(input())

sequence = list(map(input().split()))

NGEs = [-1]

max_element = sequence[-1]

for i in range(N - 2, -1, -1):
    if sequence[i] < sequence[i + 1]:
        NGEs.append(sequence[i + 1])
    elif sequence[i] >= max_element:
        NGEs.append(-1)
        max_element = sequence[i]
    else:
        for j in range(len(NGEs) - 1, -1, -1):
            if sequence[i] < NGEs[j]:
                NGEs.append(NGEs[j])
                break
        
while NGEs:
    print(NGEs.pop(), end=' ')
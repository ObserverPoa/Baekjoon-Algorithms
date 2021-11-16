import sys

sequence_size = int(sys.stdin.readline().split()[0])

sequence = list(map(int, sys.stdin.readline().split()))

NGEs = [-1] # 오큰수들

max_element = sequence[-1]

# 수열의 뒤에서부터 앞으로 탐색하며 오큰수를 구한다 
for i in range(sequence_size - 2, -1, -1):
    if sequence[i] < sequence[i + 1]: # 현재 원소의 오큰수가 바로 우측의 원소일 때
        NGEs.append(sequence[i + 1])
    elif sequence[i] >= max_element: # 현재 원소의 오큰수가 없을 때
        NGEs.append(-1)
        max_element = sequence[i]
    else: # 그 외의 경우, NGEs를 뒤로 탐색하며 현재 원소의 오큰수를 찾는다.
        for j in range(len(NGEs) - 1, -1, -1):
            if sequence[i] < NGEs[j]:
                NGEs.append(NGEs[j])
                break
        
while NGEs:
    print(NGEs.pop(), end=' ')

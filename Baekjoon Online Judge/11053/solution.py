import sys

input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))

max_lens = [] # 해당 원소를 마지막으로 갖는 증가하는 부분 순열의 최대 길이 
for i in range(N):
    max_len = 0
    for j in range(i): # 현재 숫자보다 왼쪽에 있으며 더 작은 수 중 최대 길이를 찾는다.
        if sequence[j] < sequence[i]:
            max_len = max(max_lens[j], max_len)
    max_lens.append(max_len + 1)

print(max(max_lens))
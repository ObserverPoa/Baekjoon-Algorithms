import sys

input = sys.stdin.readline

N = int(input())

sequence = list(map(int, input().split()))


max_sum = sequence[0]
current_sum = sequence[0]

for i in range(1, N):
    num = sequence[i]
    # 현재 요소를 포함해서 합을 계속하거나, 새로운 부분 배열을 시작
    current_sum = max(num, current_sum + num)
    # 최대 합 갱신
    max_sum = max(max_sum, current_sum)

print(max_sum)
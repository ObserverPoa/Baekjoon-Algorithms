import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
broken_buttons = input().strip().split() if M > 0 else []

min_pushes = abs(N - 100) # +, - 버튼만 눌러서 이동시

# 0~100만 채널 중 고장나지 않은 버튼을 사용해 곧바로 이동할 수 있는 경우, min_pushes 갱신
for i in range(100_0000):
    channel = str(i)
    if any(char in broken_buttons for char in channel):
        continue

    min_pushes = min(len(channel) + abs(N - i), min_pushes)

print(min_pushes)


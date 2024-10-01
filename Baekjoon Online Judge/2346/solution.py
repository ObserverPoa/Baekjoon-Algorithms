'''
원형 큐를 사용해서 풍선의 숫자에 따라 큐를 회전시키고 풍선을 한개씩 제거한다.
'''
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

balloons = deque(enumerate(map(int, input().split()), 1)) # 원형 큐

while True:
    num, movement = balloons.popleft()
    print(num, end=" ")
    if not balloons: break
    
    if movement > 0:
        for _ in range(movement - 1):
            balloons.append(balloons.popleft())
    else:
        for _ in range(-movement):
            balloons.appendleft(balloons.pop())

print()

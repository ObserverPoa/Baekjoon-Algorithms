'''
순환 큐에서 K번째 원소를 제거하는것을 반복한다.
'''
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque(range(1, N + 1)) # 순환 큐
sequence = [] # 수열

while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())
    sequence.append(queue.popleft())

print(f"<{', '.join(map(str, sequence))}>")

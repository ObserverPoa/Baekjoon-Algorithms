import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([(N, 0)])
visited = set()

while queue:
    cur, seconds = queue.popleft()
    visited.add(cur)

    if cur == K:
        print(seconds)
        break

    if K < cur:
        nexts = [cur - 1]
    else:
        nexts = [cur - 1, cur + 1, cur * 2]

    for next in nexts:
        if next not in visited:
            queue.append((next, seconds + 1))
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([(N, 0)])
visited = [False] * 100001
visited[N] = True
parents = [-1] * 100001

while queue:
    point, distance = queue.popleft()
    if point == K:
        min_distance = distance
        break

    for next_point in [point + 1, point - 1, point * 2]:
        if not (0 <= next_point <= 100000): continue
        if visited[next_point]: continue

        visited[next_point] = True
        parents[next_point] = point
        queue.append((next_point, distance + 1))

path = [K]
node = K

# 부모 지점을 역추적
while parents[node] != -1:
    node = parents[node]
    path.append(node)

path.reverse()
print(min_distance)
print(' '.join(map(str, path)))

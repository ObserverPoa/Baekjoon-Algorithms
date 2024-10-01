'''
bfs를 통해 최단거리가 K인 모든 도시를 찾는다.
'''
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = set([X])
queue = deque([(X, 0)])
matched_cities = [] # 최단거리가 K인 모든 도시

# BFS
while queue:
    city, distance = queue.popleft()
    if distance == K:
        matched_cities.append(city)
        continue

    for neighbor in graph[city]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, distance + 1))

if matched_cities:
    for city in sorted(matched_cities):
        print(city)
else:
    print(-1)
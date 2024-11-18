import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())

graph = defaultdict(list)

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


queue = deque([1])
parents = [0] * (N + 1) # 부모노드 및 방문 여부 확인용
parents[1] = 1

# 루트노드 부터 bfs를 해서 부모노드를 구한다.
while queue:
    node = queue.popleft()
    for child in graph[node]:
        if parents[child] == 0:
            parents[child] = node
            queue.append(child)

for i in range(2, N + 1):
    print(parents[i])


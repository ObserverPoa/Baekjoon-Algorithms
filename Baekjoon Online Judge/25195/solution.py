'''
사이클이 없는 방향그래프를 시작 노드에서 탐색을 하는데,
팬클럽이 있는 노드를 방문하면 해당 노드에서는 더 이상 탐색을 하지 않고,
이웃이 없는 노드를 방문하면 즉시 yes를 출력하고, 한번도 빙문하지 못했다면 Yes를 출력한다.
'''
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)

S = int(input())
fans = set(map(lambda x: int(x) - 1, input().split()))

def bfs(start):
    queue = deque([start])
    visited = [False] * N

    while queue:
        node = queue.popleft()
        visited[node] = True

        # 팬클럽이 있는 노드인 경우
        if node in fans:
            continue
        
        # 이웃이 없는 노드인 경우
        if not graph[node]:
            return 'yes'
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)

    return 'Yes' # 이웃이 없는 노드를 한번도 방문하지 못한 경우

print(bfs(0))
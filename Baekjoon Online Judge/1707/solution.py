'''
모든 정점이 연결되어있지 않을 수 있다.
모든 부분 그래프에 대해 bfs를 수행한다.
bfs 수행 시, 자신과 인접헌 노드는 모두 반대 그룹에 속한다고 기록하며,
이미 기록된 그룹과 다를 경우 bipartite graph가 아니다.
'''
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(graph, visited, start):
    visited.add(start)
    queue = deque([start])
    groups = { start: 'A' }

    while queue:
        node = queue.popleft()

        opposite_group = 'B' if groups[node] == 'A' else 'A'

        for neighbor in graph[node]:
            if neighbor in groups and groups[neighbor] != opposite_group:
                return False
            if neighbor in visited: 
                continue
            
            groups[neighbor] = opposite_group
            visited.add(neighbor)
            queue.append(neighbor)

    return True

def is_bipartite_graph(graph, n):
    visited = set()

    for start in range(1, n + 1):
        if start in visited: 
            continue
        if not bfs(graph, visited, start):
            return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    if is_bipartite_graph(graph, V):
        print('YES')
    else:
        print('NO')


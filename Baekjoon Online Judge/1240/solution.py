'''
양방향 그래프를 생성하고, 두 노드 쌍의 거리를 구하기 위해, 
한 노드에서 탐색을 시작해서 다른 노드를 만나면 탐색을 종료하고 그때의 이동거리를 반환한다.
'''
import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(dict)

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u][v] = graph[v][u] = w

# node에서 target까지의 거리를 반환하는 함수
def dfs(node, target, distance, visited: set):
    if node == target:
        return distance
    visited.add(node)

    for neighbor, weight in graph[node].items():
        if neighbor not in visited:
            total_distance = dfs(neighbor, target, distance + weight, visited)

            # target 노드를 하위 함수 호출에서 이미 만난 경우 즉시 리턴
            if total_distance is not None: 
                return total_distance
    return

for _ in range(M):
    u, v = map(int, input().split())
    print(dfs(u, v, 0, set()))
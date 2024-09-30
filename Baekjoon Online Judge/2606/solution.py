'''
defaultdict(list)에 그래프를 저장하고,
그래프 탐색을 통해 1번 컴퓨터가 속한 네트워크의 크기를 구한다.
'''
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

vertex_count = int(input())

graph = defaultdict(list)

for _ in range(vertex_count):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# dfs를 해서 node가 속한 그래프의 정점 개수를 반환하는 함수
def dfs(node, visited: set):
    if node in visited:
        return 0
    
    visited.add(node)

    return 1 + sum([
        dfs(v, visited) for v in graph[node]
    ])

print(dfs(1, set()) - 1) # 1번 컴퓨터 제외 처리

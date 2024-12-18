import sys
from collections import defaultdict

input = sys.stdin.readline

def check_if_possible(n, graph):
    edges = []
    for u in graph:
        for v in graph[u]:
            if u == v and graph[u][v] < 0:
                return True
            if u != v:
                edges.append((u, v))
    
    min_distances = [10000000] * (n + 1)
    min_distances[1] = 0
    
    for i in range(n):
        for u, v in edges:
            if min_distances[u] + graph[u][v] < min_distances[v]:
                min_distances[v] = min_distances[u] + graph[u][v]
                if i == n - 1:
                    return True
    return False


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = defaultdict(lambda: defaultdict(lambda : float('inf')))

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S][E] = min(graph[S][E], T)
        graph[E][S] = min(graph[E][S], T)
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S][E] = min(graph[S][E], -T)

    if check_if_possible(N, graph):
        print("YES")
    else:
        print("NO")


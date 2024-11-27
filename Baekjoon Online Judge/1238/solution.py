'''
다익스트라는 한 노드에서 다른 모든 노드로의 최단거리를 구하는 방법인데,
그냥 하면 다익스트라를 N + 1번 해야 하기 떄문에,
원래 그래프는 X에서 각 집으로 돌아가는 최소 시간을,
간선 방향을 뒤집은 그래프는 각 집에서 X로 가는 최소 시간을 구하는데 사용한다.
두 그래프 둘다 X 노드로부터 다익스트라를 한번씩만 하면 답을 구할 수 있다.
'''
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = defaultdict(dict)
reversed_graph = defaultdict(dict) # 간선 방향을 뒤집은 그래프

for _ in range(M):
    v, w, t = map(int, input().split())
    graph[v][w] = t
    reversed_graph[w][v] = t

# 다익스트라
# graph의 각 노드의 start 노드와의 최단시간 리스트 반환
def dijkstra(start, graph):
    pq = [(0, start)]
    min_times = [float('inf') for _ in range(N + 1)]
    min_times[start] = 0

    while pq:
        time, node = heapq.heappop(pq)
        if min_times[node] < time: continue

        for neighbor in graph[node]:
            next_time = time + graph[node][neighbor]
            if next_time < min_times[neighbor]:
                min_times[neighbor] = next_time
                heapq.heappush(pq, (next_time, neighbor))
    
    return min_times


max_time = float('-inf')
for t1, t2 in zip(dijkstra(X, graph), dijkstra(X, reversed_graph)):
    if t1 == float('inf'): continue # 0번 인덱스 건너뛰기

    if max_time < t1 + t2:
        max_time = t1 + t2

print(max_time)



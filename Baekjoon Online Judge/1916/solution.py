import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

A, B = map(int, input().split())

# 다익스트라
pq = []
min_total_costs = [float('inf')] * (N + 1)
heapq.heappush(pq, (0, A))
min_total_costs[A] = 0

while pq:
    total_cost, city = heapq.heappop(pq)
    if total_cost > min_total_costs[city]: continue

    for next_city, cost in graph[city]:
        next_total_cost = total_cost + cost
        if next_total_cost < min_total_costs[next_city]:
            min_total_costs[next_city] = next_total_cost
            heapq.heappush(pq, (next_total_cost, next_city))

print(min_total_costs[B])

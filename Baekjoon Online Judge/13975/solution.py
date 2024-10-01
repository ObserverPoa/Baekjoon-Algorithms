import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    sizes = list(map(int, input().split()))
    heapq.heapify(sizes)

    total_cost = 0

    while len(sizes) >= 2:
        size1 = heapq.heappop(sizes)
        size2 = heapq.heappop(sizes)
        cost = size1 + size2
        total_cost += cost
        heapq.heappush(sizes, cost)

    print(total_cost)


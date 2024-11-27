import sys
import heapq

input = sys.stdin.readline

N = int(input())

max_pq = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if max_pq:
            print(-heapq.heappop(max_pq))
        else:
            print(0)
    else:
        heapq.heappush(max_pq, -x)

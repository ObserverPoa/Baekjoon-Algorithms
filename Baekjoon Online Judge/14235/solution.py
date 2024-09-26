'''
min heap을 사용하므로, 
매번 가장 큰 가치가 pop 되도록 priority queue에 가치를 음수로 저장한다.
'''
import sys
import heapq

input = sys.stdin.readline

N = int(input())

pq = [] # priority queue

for _ in range(N):
    args = list(map(int, input().split()))

    if args[0] > 0:
        for i in range(1, len(args)):
            heapq.heappush(pq, -args[i])
    else:
        print(-heapq.heappop(pq) if pq else -1)
    
'''
priority queue에 자연수를 추가하거나 가장 작은 수를 제거해서 출력한다.
'''
import sys
import heapq

input = sys.stdin.readline

N = int(input())

pq = [] # priority queue

for _ in range(N):
    x = int(input())

    if x > 0:
        heapq.heappush(pq, x)
    elif x == 0:
        print(heapq.heappop(pq) if pq else 0)
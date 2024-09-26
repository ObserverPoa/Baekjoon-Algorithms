'''
우선순위 큐를 사용해서 가장 작은 두 수를 계속 더해간다.
큰 수를 최대한 나중에 더해야 뒷 단계에 미치는 영향을 최소화할 수 있다.
'''
import sys
import heapq

input = sys.stdin.readline

N = int(input())

pq = []
for _ in range(N):
    heapq.heappush(pq, int(input()))

answer = 0
while len(pq) > 1:
    a, b = heapq.heappop(pq), heapq.heappop(pq)
    compares = a + b
    answer += compares
    heapq.heappush(pq, compares)

print(answer)
'''
좌표를 순서대로 왼쪽부터 읽어가면서, 
y가 0이 아니고 y에 진행중인 건물이 없다면 새로운 건물을 시작하고,
y보다 더 높은 건물을 모두 끝내고 그 개수만큼 카운팅에 더한다.
'''
import sys
import heapq

input = sys.stdin.readline

N = int(input())

count = 0
max_pq = [] # max priority queue

for _ in range(N):
    _, y = map(int, input().split())

    # y보다 더 높은 건물을 모두 끝내고 그 개수만큼 카운팅에 더한다
    while max_pq and -max_pq[0] > y:
        heapq.heappop(max_pq)
        count += 1

    # y가 0이 아니고 y에 진행중인 건물이 없다면
    if y > 0 and (not max_pq or -max_pq[0] < y):
        heapq.heappush(max_pq, -y)

count += len(max_pq)

print(count)


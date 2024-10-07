'''
구해야 하는 값은, 동시에 진행중인 최대 강의 개수이다.
시작시간 오름차순으로 정렬하고, 강의실을 한개씩 배정하며, 그 전에, 현재 시간에서 비워진 강의실을 처리한다.
강의실을 점유할때 끝나는 시간을 우선순위 큐에 넣는다.
'''
import sys
import heapq

input = sys.stdin.readline

N = int(input())

lectures = [list(map(int, input().split())) for _ in range(N)]

pq = [] # priorty queue

count = 0
max_count = 0

for _, start, end in sorted(lectures, key=lambda x: x[1]):
    while pq and pq[0] <= start:
        heapq.heappop(pq)
        count -= 1

    count += 1
    max_count = max(max_count, count)
    heapq.heappush(pq, end)

print(max_count)
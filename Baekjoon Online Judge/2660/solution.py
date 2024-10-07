'''
다익스트라 알고리즘을 사용해서 모든 회원의 점수를 구하고,
최소 점수를 갖는 회원들을 출력한다.
'''
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

graph = defaultdict(list) # 양방향 그래프

while True:
    u, v = map(int, input().split())
    if u == v == -1: 
        break
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)


# 다익스트라 알고리즘
def find_max_distance(start_node):
    pq = [(0, start_node)] # priority queue
    min_distances = [N] * N

    while pq:
        distance, node = heapq.heappop(pq)
        if distance >= min_distances[node]: 
            continue

        min_distances[node] = distance

        for neighbor in graph[node]:
            if distance + 1 < min_distances[neighbor]:
                heapq.heappush(pq, (distance + 1, neighbor))

    return max(min_distances)


min_score = N # 회장 후보의 점수
min_score_members = [] # 회장 후보

for i in range(N):
    score = max(1, find_max_distance(i))
    if score < min_score:
        min_score = score
        min_score_members = [i + 1]
    elif score == min_score:
        min_score_members.append(i + 1)
    
print(f'{min_score} {len(min_score_members)}')
print(' '.join(map(str, min_score_members)))
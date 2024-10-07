'''
플로이드 워셜 알고리즘을 사용해서, 
모든 행성간의 최소 거리를 구하고, 
K에서 시작해서 다른 모든 노드를 방문하는 전체 경우의 수를 따져서 최소 소요 시간을 구한다.
'''
import sys
from itertools import permutations

input = sys.stdin.readline

N, K = map(int, input().split())

times = [ list(map(int, input().split())) for _ in range(N) ]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if times[i][j] > times[i][k] + times[k][j]:
                times[i][j] = times[i][k] + times[k][j]

min_total_time = float('inf')

for nodes in permutations([i for i in range(N) if i != K]):
    total_time = 0
    prev_node = K
    for node in nodes:
        total_time += times[prev_node][node]
        prev_node = node
    min_total_time = min(min_total_time, total_time)

print(min_total_time)
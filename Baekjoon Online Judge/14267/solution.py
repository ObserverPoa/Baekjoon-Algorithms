'''
상사와 부하 관계로 트리를 생성하고,
초기 칭찬 수치 배열을 초기화 하고,
트리의 루트노드에서 bfs를 하면서 
칭찬 수치를 부하 노드에 누적시켜간다.
'''
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = map(int,input().split())

parents = list(map(int, input().split()))

total_sums = [0] * (N + 1)
for _ in range(M):
    i, w = map(int, input().split())
    total_sums[i] += w

tree = defaultdict(list)
for child, parent in enumerate(parents, 1):
    tree[parent].append(child)


queue = deque([1])
while queue:
    node = queue.popleft()

    for child in tree[node]:
        total_sums[child] += total_sums[node]
        queue.append(child)

for total_sum in total_sums[1:]:
    print(total_sum, end=" ")








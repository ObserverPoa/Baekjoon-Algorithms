'''
노드 간의 간선들을 최소 비용으로 사용해서 모든 노드가 연결되도록 해야 한다.
모든 노드가 연결되려면 최소 N-1개의 간선을 사용해야 한다.
가장 작은 비용의 간선부터 계속 확인해서, 
두 정점이 다른 경로를 통해 연결되어 있지 않으면 연결하고, 모든 노드가 연결되었을때 중단한다.
'''
import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

pq = []
for _ in range(M):
    a, b, c = map(int, input().split())
    pq.append((c, a - 1, b - 1))
heapq.heapify(pq)

roots = list(range(N)) # 각 노드가 속한 트리의 루트 노드

# 모든 노드가 연결되었는지 확인
def all_connected():
    for i in range(1, N):
        if roots[0] != roots[i]:
            return False
    return True

cost = 0
while pq and not all_connected():
    c, a, b = heapq.heappop(pq)
    # 불필요한 간선거나, 이미 두 노드가 연결되어있는 경우
    if a == b or roots[a] == roots[b]:
        continue
    
    # a 트리로 합쳐질 대상 트리의 루트 노드
    merged_root = roots[b] 
    for i in range(N):
        if roots[i] == merged_root:
            roots[i] = roots[a]

    cost += c

print(cost)
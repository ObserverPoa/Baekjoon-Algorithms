import sys
from collections import defaultdict

input = sys.stdin.readline

N, D = map(int, input().split())

shortcuts = defaultdict(dict)

nodes = set([0, D]) # 모든 노드 (시작노드, 끝 노드, 지름길 양쪽 노드)

for _ in range(N):
    low, high, distance = map(int, input().split()) # low: 시작노드, high: 종료노드
    if high > D: continue # 지름길 종료 노드가 끝 노드 뒤라면, 유효하지 않은 지름길
    if high - low <= distance: continue # 지름길이 그냥 가는것보다 더 짧지 않다면, 의미 없는 지름길

    nodes.add(low)
    nodes.add(high)

    # low에서 high까지 가는 가장 짧은 지름길만 저장
    if high in shortcuts[low]:
        shortcuts[low][high] = min(distance, shortcuts[low][high])
    else:
        shortcuts[low][high] = distance


min_distances = defaultdict(lambda : float('inf')) # 시작노드로부터의 최소 거리
min_distances[0] = 0

nodes = list(sorted(nodes))

# 모든 노드를 작은 것 부터 순차적으로 탐색하며 최소 거리를 갱신한다.
# 항상 작은 노드로부터 큰 노드로만 이동할 수 있기 때문에 pq가 필요없다.
for i in range(len(nodes)):
    node = nodes[i]
    min_distance_from_zero = min_distances[node]

    # 한단계 더 큰 노드에 대해, 현재 노드에서 지름길을 사용하지 않고 이동했을 때의 최소 거리 갱신
    if i < len(nodes) - 1:
        min_distances[nodes[i + 1]] = min(
            min_distances[nodes[i + 1]], 
            min_distance_from_zero + (nodes[i + 1] - node)
        )
    
    # 현재 노드가 시작점인 모든 지름길에 대해 도착지의 최소 거리 갱신
    for high in shortcuts[node]:
        min_distances[high] = min(
            min_distances[high], 
            min_distance_from_zero + shortcuts[node][high]
        )

print(min_distances[D])
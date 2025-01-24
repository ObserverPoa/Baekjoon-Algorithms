'''
트리의 지름을 구성하는 두 노드는 반드시 모두 리프노드이다.
중간노드로 설정하면 무조건 손해이기 때문이다.
'''
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)

for _ in range(n - 1):
    u, v, weight = map(int, input().split())
    tree[u].append((v, weight))
    tree[v].append((u, weight))

# 루트노드 (1) 을 기준으로 각 노드의 depth 구하기
nodes = [(1, 0)]
queue = deque(nodes)
visited = set([1])
while queue:
    node, depth = queue.popleft()
    for neighbor, _ in tree[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, depth + 1))
            nodes.append((neighbor, depth + 1))

max_distance = 0 # 트리의 지름
longest_distances_to_leaf = {} # 특정 노드의 자손 리프노드까지의 최장 거리

# 각 노드의 depth가 큰 순서대로 리프노드까지의 최대 거리를 구하고, 지름을 갱신
for node, _ in sorted(nodes, key=lambda x: -x[1]):
    distances_to_leaf = [] # 현재 노드의 자식 노드들을 통한 자손 리프노드까지의 거리들
    for neighbor, weight in tree[node]:
        if neighbor in longest_distances_to_leaf: # 현재 노드의 자식 노드는 모두 True
            distances_to_leaf.append(longest_distances_to_leaf[neighbor] + weight)
    
    distances_to_leaf.sort(reverse=True)

    # 현재 노드의 자식 노드 중 한개에서 다른 자식 노드로 가는 거리로 max_distance를 갱신
    max_distance = max(sum(distances_to_leaf[:2]), max_distance)

    # 현재 노드의 자손 리프노드까지의 최대 거리 저장
    longest_distances_to_leaf[node] = distances_to_leaf[0] if distances_to_leaf else 0

print(max_distance)


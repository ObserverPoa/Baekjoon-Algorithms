import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

graph = defaultdict(set)
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

groups = [] # 최종 그룹 목록
children = defaultdict(list) # 각 노드의 자손 중 아직 그룹을 형성하지 못한 자손 목록

leaf_nodes = [v for v in graph if len(graph[v]) == 1]

# 리프 노드들을 그래프에서 분리시켜나간다.
while leaf_nodes:
    next_leaf_nodes = set()

    for leaf in leaf_nodes: 
        child_count = len(children[leaf])
        # 3개씩 그룹지을 수 없는 경우
        if child_count > 2: 
            next_leaf_nodes = None
            break

        # 그룹 형성이 가능한 경우
        if child_count == 2:
            children[leaf].append(leaf)
            groups.append(children[leaf])
            # groups.append((leaf, *children[leaf])) # 이 코드를 대신 사용하면 오답처리되는데, 원인을 알 수 없음

        # 부모가 없는 노드인 경우 (마지막으로 남은 노드)
        if not graph[leaf]:
            break

        parent = graph[leaf].pop() # 리프 노드의 부모

        # 그룹 형성을 위한 자식이 부족한 경우, 부모에 위임한다.
        if child_count < 2:
            children[parent].append(leaf)
            children[parent].extend(children[leaf])

        graph[parent].remove(leaf) # 리프 노드를 그래프에서 분리

        # 부모 노드가 리프 노드인 경우 목록에 추가
        if len(graph[parent]) <= 1:
            next_leaf_nodes.add(parent)

    leaf_nodes = next_leaf_nodes
    
if len(groups) == N // 3:
    print('S')
    for group in groups:
        print(' '.join(map(str, group)))
else:
    print('U')


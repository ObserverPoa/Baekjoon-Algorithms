import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N = int(input())

tree = defaultdict(list)

for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visit_order = list(map(int, input().split()))

def is_valid_visit_order(start_node, visit_order: list[int]):
    if visit_order[0] != start_node:
        return False

    visited = [False] * (N + 1) 
    queue = deque([start_node])
    visited[start_node] = True
    
    idx = 1

    while queue:
        node = queue.popleft()

        # 모든 자식 노드들을 다음에 방문해야 하며, 그 자식노드들 간의 방문 순서는 상관없다.
        # 그래서 정렬 후 tuple이 같은지를 비교한다.
        child_nodes = []
        for neigbor in tree[node]:
            if visited[neigbor]: continue

            visited[neigbor] = True
            child_nodes.append(neigbor)
        sorted_child_nodes = tuple(sorted(child_nodes))

        child_visit_order = visit_order[idx:idx + len(child_nodes)]
        idx += len(child_nodes)

        if sorted_child_nodes != tuple(sorted(child_visit_order)):
            return False

        # child_nodes가 아닌, child_visit_order로 extend해야 올바른 검사가 가능하다.
        queue.extend(child_visit_order)
    
    return True


if is_valid_visit_order(1, visit_order):
    print(1)
else:
    print(0)
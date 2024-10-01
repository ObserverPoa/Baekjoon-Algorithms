import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(lambda: defaultdict(int))
for _ in range(M):
    u, v, limit = map(int, input().split())
    
    graph[u][v] = max(graph[u][v], limit)
    graph[v][u] = max(graph[v][u], limit)

start, end = map(int, input().split())


# bfs를 사용해서 weight로 start에서 end까지 도달 가능한지 여부를 반환
def reachable(weight):
    queue = deque([start])
    visited = set([start])

    while queue:
        island = queue.popleft()
        if island == end:
            return True
        
        for neighbor, limit in graph[island].items():
            if neighbor not in visited and weight <= limit:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


# binary search를 사용헤서 최대 중량을 찾는다.
def find_max_weight():
    left = 1
    right = 1_000_000_000

    while left <= right:
        mid = (left + right) // 2

        if reachable(mid):
            left = mid + 1
        else:
            right = mid - 1
    
    return right

print(find_max_weight())
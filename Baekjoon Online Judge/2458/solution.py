'''
자신의 키가 몇 번째인지 알 수 있으려면,
나를 제외한 모든 노드는 내가 방문할 수 있거나, 방문당할 수 있는 노드여야 한다.
모든 노드에서 한번씩 그래프 탐색을 수행하는데, 방문할 떄 마다 자신의 카운터와 방문한 노드의 카운터를 1씩 증가시킨다.
최종적으로 카운터들을 확인했을때, 카운팅이 N - 1인 노드들이 자신의 키가 몇번째인지 정확하게 알 수 있는 노드이다.
'''
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

connection_counter = defaultdict(int) # 각 노드에 대해, 다른노드가 자신을 방문한 횟수 + 내가 다른 노드를 방문한 횟수

def bfs(start):
    queue = deque([start])
    visited = [False] * (N + 1)

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                connection_counter[start] += 1
                connection_counter[neighbor] += 1
                queue.append(neighbor)

for i in range(1, N + 1):
    bfs(i)

answer = 0
for count in connection_counter.values():
    if count == N - 1:
        answer += 1
print(answer)

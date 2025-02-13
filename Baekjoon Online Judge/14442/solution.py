import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

grid = [ [int(char) for char in input().strip()] for _ in range(N) ]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

queue = deque([(0, 0, 1, 0)])
visited = [[-1] * M for _ in range(N)] # 방문했을때까지 벽을 부순 횟수의 최소값 (-1 이면 미방문)
visited[0][0] = 0

min_distance = float('inf')

while queue:
    x, y, distance, broken_count = queue.popleft()
    if x == N - 1 and y == M - 1:
        min_distance = min(distance, min_distance)
        break

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not (0 <= nx < N and 0 <= ny < M): continue
        if grid[nx][ny] == 1 and broken_count == K: continue # 벽인데 파괴횟수를 모두 소진한 경우 스킵

        # 벽 인지 여부에 따라 다음 파괴 횟수 설정
        next_broken_count = broken_count
        if grid[nx][ny] == 1:
            next_broken_count += 1
        
        # 방문한적이 있고, 새로운 파괴횟수가 더 적지 않다면 스킵
        if visited[nx][ny] != -1 and visited[nx][ny] <= next_broken_count: continue

        visited[nx][ny] = next_broken_count
        queue.append((nx, ny, distance + 1, next_broken_count))
        

if min_distance == float('inf'):
    print(-1)
else:
    print(min_distance)
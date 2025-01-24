import sys
from collections import deque

input = sys.stdin.readline

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

N = int(input())

grid = [ list(map(int, input().split())) for _ in range(N) ]

visited = [[False] * N for _ in range(N)]

def explore_island(sx, sy):
    island_coords = [(sx, sy)]
    queue = deque([(sx, sy)])
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N): continue
            if grid[nx][ny] == 0: continue
            if visited[nx][ny]: continue

            visited[nx][ny] = True
            queue.append((nx, ny))
            island_coords.append((nx, ny))

    return island_coords

islands = []

for x in range(N):
    for y in range(N):
        if not visited[x][y] and grid[x][y] != 0: 
            islands.append(explore_island(x, y))

for i, island_coords in enumerate(islands, 1):
    for x, y in island_coords:
        grid[x][y] = i

min_bridge_length = float('inf')

for i, island_coords in enumerate(islands, 1):
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    for x, y in island_coords:
        visited[x][y] = True
        queue.append((x, y, -1))

    while queue:
        x, y, bridge_length = queue.popleft()
        if grid[x][y] != 0 and grid[x][y] != i:
            min_bridge_length = min(bridge_length, min_bridge_length)
            break

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N): continue
            if visited[nx][ny]: continue

            visited[nx][ny] = True
            queue.append((nx, ny, bridge_length + 1))

print(min_bridge_length)
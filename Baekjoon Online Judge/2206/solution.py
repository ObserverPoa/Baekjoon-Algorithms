import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [
    [int(cell) for cell in input().strip()]
    for _ in range(N)
]

def in_grid(x, y):
    return 0 <= x < N and 0 <= y < M

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]


def bfs(start, end):
    queue = deque([(*start, 1, False)])
    visited = [[0] * M for _ in range(N)] # 0: 미방문, 1: 꺤 적이 있는 상태로 방문, 2: 깬 적이 없는 상태로 방문
    visited[start[0]][start[1]] = 0

    while queue:
        x, y, distance, broken = queue.popleft()
        if (x, y) == end:
            return distance

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_grid(nx, ny): continue
            if visited[nx][ny] == 2: continue
            if visited[nx][ny] == 1 and broken: continue
            if broken and grid[nx][ny] == 1: continue

            visited[nx][ny] = 1 if broken else 2
            queue.append((nx, ny, distance + 1, True if grid[nx][ny] == 1 else broken))

    return -1

print(bfs((0, 0), (N - 1, M - 1)))




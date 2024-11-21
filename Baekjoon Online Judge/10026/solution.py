import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

grid = [
    [char for char in input().strip()]
    for _ in range(N)
]

def in_grid(x, y):
    return 0 <= x < N and 0 <= y < N

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def visit_district(sx, sy, visited, color_group = []):
    queue = deque([(sx, sy)])
    visited[sx][sy] = True

    color = grid[sx][sy]
    allowed_colors = color_group if color in color_group else [color]

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_grid(nx, ny): continue
            if grid[nx][ny] not in allowed_colors: continue
            if visited[nx][ny]: continue

            visited[nx][ny] = True
            queue.append((nx, ny))


def count_districts(color_group = []):
    visited = [[False] * N for _ in range(N)]
    count = 0
    for x in range(N):
        for y in range(N):
            if visited[x][y]: continue
                
            visit_district(x, y, visited, color_group)
            count += 1
    return count


normal_count = count_districts()
blind_count = count_districts(['R', 'G'])
print(f"{normal_count} {blind_count}")


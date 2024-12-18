import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [ list(map(int, input().split())) for _ in range(N) ]

H, W, Sx, Sy, Fx, Fy = map(int, input().split())
Sx -= 1
Sy -= 1
Fx -= 1
Fy -= 1

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# 위로 이동하는 경우, 윗변을 가져오는 방식
front_side_getters = [
    lambda left_top: [grid[left_top[0]][y] for y in range(left_top[1], left_top[1] + W)],
    lambda left_top: [grid[x][left_top[1] + W - 1] for x in range(left_top[0], left_top[0] + H)],
    lambda left_top: [grid[left_top[0] + H - 1][y] for y in range(left_top[1], left_top[1] + W)],
    lambda left_top: [grid[x][left_top[1]] for x in range(left_top[0], left_top[0] + H)],
]

def bfs():
    queue = deque([(Sx, Sy, 0)])
    visited = [[False] * M for _ in range(N)] # 방문한 좌표인지 (사각형의 왼쪽 위 좌표 기준)
    visited[Sx][Sy] = True

    while queue:
        x, y, step = queue.popleft()

        for dx, dy, get_front_side in zip(dxs, dys, front_side_getters):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N - H + 1 and 0 <= ny < M - W + 1): continue
            if visited[nx][ny]: continue
            if 1 in get_front_side((nx, ny)): continue

            if nx == Fx and ny == Fy:
                return step + 1
            
            visited[nx][ny] = True
            queue.append((nx, ny, step + 1))

    return -1

print(bfs())
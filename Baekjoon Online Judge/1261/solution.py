import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

maze = [
    [int(char) for char in input().strip()]
    for _ in range(N)
]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

queue = deque([(0, 0)])

# -1: 미방문, not -1: (0, 0)에서 (x, y)까지 가기 위한 최소 부수기 횟수
counter = [[-1] * M for _ in range(N)] 
counter[0][0] = 0

while queue:
    x, y = queue.popleft()

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if not (0 <= nx < N and 0 <= ny < M): continue

        if counter[nx][ny] == -1 or counter[x][y] + maze[nx][ny] < counter[nx][ny]:
            counter[nx][ny] = counter[x][y] + maze[nx][ny]
            queue.append((nx, ny))

print(counter[N - 1][M - 1])
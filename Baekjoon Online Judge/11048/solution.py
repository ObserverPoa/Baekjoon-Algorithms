import sys

input = sys.stdin.readline

N, M = map(int, input().split())

maze = [ list(map(int, input().split())) for _ in range(N) ]

for i in range(1, N):
    maze[i][0] += maze[i - 1][0]

for i in range(1, M):
    maze[0][i] += maze[0][i - 1]

# 현재 칸으로 올 수 있는 칸 중 최대값을 현재 칸에 누적시킨다.
for i in range(1, N):
    for j in range(1, M):
        maze[i][j] += max(maze[i - 1][j - 1], maze[i - 1][j], maze[i][j - 1])

print(maze[N - 1][M - 1])

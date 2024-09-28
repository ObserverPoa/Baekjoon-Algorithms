'''
숫자판이 5x5 크기이고 네 방향으로 다섯 번 이동하기 때문에, 
모든 경로에 대한 완전탐색이 가능하다.
'''
import sys

input = sys.stdin.readline

N = 5

grid = [ input().strip().split() for _ in range(N) ]

# 위쪽부터 시계방향 순 (x: 행, y: 열)
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

numbers = set()

# path에는 루트노드부터 현재노드까지의 값을 기록한다.
def dfs(x, y, path: list[str]):
    path.append(grid[x][y])
    if len(path) >= 6:
        numbers.add(''.join(path))
    else:
        for dx, dy in zip(dxs, dys):
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x < N and 0 <= next_y < N:
                dfs(next_x, next_y, path)
    path.pop()

for x in range(N):
    for y in range(N):
        dfs(x, y, [])

print(len(numbers))
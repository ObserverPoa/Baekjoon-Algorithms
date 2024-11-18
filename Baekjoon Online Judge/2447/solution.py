import sys

input = sys.stdin.readline

N = int(input())

grid = [[' '] * N for _ in range(N)]
grid[0][0] = '*'

n = 1
while n < N:
    for i in range(3):
        for j in range(3):
            if i == j == 0: continue # 좌측 상단은 이미 완성된 부분이다.
            if i == j == 1: continue # 중간은 비워두는 부분이다.

            # 좌측 상단 영역을 현재 영역에 복사한다.
            for x in range(n * i, n * (i + 1)):
                for y in range(n * j, n * (j + 1)):
                    grid[x][y] = grid[x % n][y % n]
    n *= 3

for x in range(N):
    for y in range(N):
        print(grid[x][y], end="")
    print()

import sys

input = sys.stdin.readline

N = int(input())
mid = N // 2

target_num = int(input())

grid = [[0] * N for _ in range(N)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

x, y = mid, mid
num = 1
grid[x][y] = num
target_x, target_y = x, y

for i in range(1, mid + 1):
    x, y = mid - i, mid - i

    for dx, dy in zip(dxs, dys):
        for _ in range(2 * i):
            x, y = x + dx, y + dy
            num += 1
            grid[x][y] = num
            if num == target_num:
                target_x, target_y = x, y
            
for x in range(N):
    for y in range(N):
        print(grid[x][y], end = " ")
    print()

print(f'{target_x + 1} {target_y + 1}')

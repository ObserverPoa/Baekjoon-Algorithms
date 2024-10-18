import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

grid = [
    list(map(int, input().split())) for _ in range(N)
]

commands = list(map(int, input().split()))

directions = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}

dice_vertical = [0] * 4  # 하 전 상 후
dice_horizontal = [0] * 4  # 하 좌 상 우

for command in commands:
    dx, dy = directions[command]
    nx, ny = x + dx, y + dy

    if not (0 <= nx < N and 0 <= ny < M):
        continue
    x, y = nx, ny

    # 주사위 굴림 처리
    if command == 1:
        dice_horizontal.insert(0, dice_horizontal.pop())
        dice_vertical[0], dice_vertical[2] = dice_horizontal[0], dice_horizontal[2]
    elif command == 2:
        dice_horizontal.append(dice_horizontal.pop(0))
        dice_vertical[0], dice_vertical[2] = dice_horizontal[0], dice_horizontal[2]
    elif command == 3:
        dice_vertical.insert(0, dice_vertical.pop())
        dice_horizontal[0], dice_horizontal[2] = dice_vertical[0], dice_vertical[2]
    elif command == 4:
        dice_vertical.append(dice_vertical.pop(0))
        dice_horizontal[0], dice_horizontal[2] = dice_vertical[0], dice_vertical[2]

    # 주사위 바닥면 숫자를 칸에 복사하거나, 칸의 숫자를 주사위 바닥에 복사하고 칸을 0으로 만든다.
    if grid[x][y] == 0:
        grid[x][y] = dice_vertical[0]
    else:
        dice_vertical[0] = dice_horizontal[0] = grid[x][y]
        grid[x][y] = 0

    print(dice_vertical[2])

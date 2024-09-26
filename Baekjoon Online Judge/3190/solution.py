import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

K = int(input())
apple_coords = set([
    tuple(map(lambda x: x - 1, map(int, input().split())))
    for _ in range(K)
])

L = int(input())
moves = []
for _ in range(L):
    args = input().strip().split()
    moves.append([int(args[0]), args[1]])
moves.reverse()

# 오른쪽 방향부터 시계방향 순
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

game_seconds = 1
direction = 0
snake_queue = deque([(0, 0)]) # 뱀의 머리를 추가하고 꼬리를 제거하는 용도
snake_coords = set(snake_queue) # 뱀의 몸과 부딪혔는지 확인하는 용도

# 벽과 부딪혔는지 확인하는 함수
def is_valid_coord(x, y):
    return 0 <= x < N and 0 <= y < N

while True:
    x, y = snake_queue[0]
    new_head = (x + dxs[direction], y + dys[direction])
    
    # 새롭게 늘리려는 머리가 유효한지 확인
    if new_head in snake_coords or not is_valid_coord(*new_head):
        break
    
    # 머리를 늘린다.
    snake_queue.appendleft(new_head)
    snake_coords.add(new_head)

    # 사과가 있으면 사과를 제거하고, 없으면 꼬리를 제거
    if new_head not in apple_coords:
        tail = snake_queue.pop()
        snake_coords.remove(tail)
    else:
        apple_coords.remove(new_head)
    
    # 방향 전환 처리
    if moves and moves[-1][0] == game_seconds:
        _, move = moves.pop()
        if move == 'L':
            direction = 3 if direction == 0 else direction - 1
        elif move == 'D':
            direction = (direction + 1) % 4

    game_seconds += 1

print(game_seconds)


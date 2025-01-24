import sys
from collections import defaultdict

input = sys.stdin.readline

N, M, K = map(int, input().split())

fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r - 1, c - 1, m, s, d))

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

def move(point, amount):
    destination = (point + amount) % N
    if destination < 0:
        destination += N
    return destination

for _ in range(K):
    fireballs_by_coord = defaultdict(list)

    for x, y, m, s, d in fireballs:
        nx, ny = move(x, dxs[d] * s), move(y, dys[d] * s)
        fireballs_by_coord[(nx, ny)].append((m, s, d))

    next_fireballs = []
    for coord, fireball_list in fireballs_by_coord.items():
        if len(fireball_list) >= 2:
            mass = sum(map(lambda item: item[0], fireball_list)) // 5
            if mass == 0:
                continue
            
            speed = sum(map(lambda item: item[1], fireball_list)) // len(fireball_list)

            directions = [1, 3, 5, 7]
            if all(map(lambda item: item[2] % 2 == 0, fireball_list)) \
                or all(map(lambda item: item[2] % 2 == 1, fireball_list)):
                directions = [0, 2, 4, 6]
            
            for direction in directions:
                next_fireballs.append((*coord, mass, speed, direction))
        else:
            next_fireballs.append((*coord, *fireball_list[0]))

    fireballs = next_fireballs

print(sum(map(lambda item: item[2], fireballs)))
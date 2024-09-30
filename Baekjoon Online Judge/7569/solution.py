'''
3차원 BFS를 한다. 새롭게 익은 토마토가 없고, 아직 안익은 토마토가 있을때 까지 반복한다.
다음으로 익을 토마토의 좌표 후보는, 새롭게 익은 토마토의 주변에만 있기 때문이다. 
'''
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

# z: 높이, x: 행, y: 열
box = [
    [ list(map(int, input().split())) for _ in range(N) ] 
    for _ in range(H)
]

def in_box(z, x, y):
    return 0 <= z < H and 0 <= x < N and 0 <= y < M

def not_ripe(z, x, y):
    return box[z][x][y] == 0

def make_ripe(z, x, y):
    box[z][x][y] = 1

tomato_count = 0
ripe_tomatoes = []

for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] != -1:
                tomato_count += 1
            if box[z][x][y] == 1:
                ripe_tomatoes.append((z, x, y))

ripe_count = len(ripe_tomatoes)

if tomato_count == ripe_count:
    print(0)
else:
    edge_tomatoes = ripe_tomatoes
    day = 0

    # 상 우 하 좌 위 아래
    dzs = [0, 0, 0, 0, 1, -1]
    dxs = [-1, 0, 1, 0, 0, 0]
    dys = [0, 1, 0, -1, 0, 0]
    
    while edge_tomatoes and ripe_count < tomato_count:
        next_edge_tomatoes = []

        for z, x, y in edge_tomatoes:
            for dz, dx, dy in zip(dzs, dxs, dys):
                neighbor = (z + dz, x + dx, y + dy)

                if in_box(*neighbor) and not_ripe(*neighbor): 
                    make_ripe(*neighbor)
                    ripe_count += 1
                    next_edge_tomatoes.append(neighbor)

        edge_tomatoes = next_edge_tomatoes
        day += 1
        
    if tomato_count == ripe_count:
        print(day)
    else:
        print(-1)

'''
이동방향의 끝에서 가까운 구슬부터 이동 처리를 한다.
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [ [char for char in input().strip()] for _ in range(N) ]

def find_coord(value):
    for x in range(N):
        for y in range(M):
            if board[x][y] == value:
                return (x, y)

# readonly
class Marble:
    def __init__(self, coord, name):
        self.x = coord[0]
        self.y = coord[1]
        self.name = name

red_marble = Marble(find_coord('R'), 'R')
blue_marble = Marble(find_coord('B'), 'B')

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# coord 에 있는 구슬을 dx, dy 방향으로 벽이나 다른 구슬을 만날때까지 또는 구멍에 빠질때까지 이동시키고,
# 이동된 좌표를 반환한다.
# marble_coords는 현재 보드에 있는 구슬들의 좌표 set이다.
def move_marble(coord, dx, dy, marble_coords):
    x, y = coord
    nx, ny = x + dx, y + dy

    while board[nx][ny] != '#' and (nx, ny) not in marble_coords:
        x, y = nx, ny
        if board[x][y] == 'O':
            break
        nx, ny = x + dx, y + dy

    return (x, y)

# 최종 정답
min_depth = float('inf')

def dfs(depth, marbles: list[Marble]):
    global min_depth
    if depth > min(10, min_depth):
        return
    
    for dx, dy in zip(dxs, dys):
        marble_coords = set(map(lambda marble: (marble.x, marble.y), marbles)) # 현재 보드에 있는 구슬들의 좌표 set

        popped_marbles: list[Marble] = []
        next_marbles: list[Marble] = []
        
        # 이동방향의 끝에서 가까운 구슬 순으로 정렬한다.
        for marble in sorted(marbles, key=lambda marble: -(marble.x * dx + marble.y * dy)):
            marble_coord = (marble.x, marble.y) # 이동하기 전 구슬의 좌표
            new_x, new_y = move_marble(marble_coord, dx, dy, marble_coords)

            marble_coords.remove(marble_coord) # 이동하기 전의 좌표를 set에서 제거

            if board[new_x][new_y] == 'O': # 구멍에 빠진 경우, popped_marbles에 구슬을 추가한다.
                popped_marbles.append(marble)
            else: # 구멍에 빠지지 않은 경우, 이동된 좌표를 set에 추가하고(이후 iteration을 위함), next_marbles에 다음 depth에서 사용할 Marble 추가
                new_coord = (new_x, new_y)
                next_marbles.append(Marble(new_coord, marble.name))
                marble_coords.add(new_coord)
        
        # 이번 기울임에서 구슬이 한개만 빠졌으며, 그것이 빨간 구슬이라면, min_depth 갱신.
        # 그렇지 않고, 구멍에 빠진 구슬이 없었다면 다음 depth로 이동 (만약 파란 구슬만 빠졌거나 구슬 두개 다 빠졌다면 계속하면 안되기 때문)
        if len(popped_marbles) == 1 and popped_marbles[0].name == 'R':
            min_depth = min(depth, min_depth)
        elif len(next_marbles) == len(marbles):
            dfs(depth + 1, next_marbles)

dfs(1, [red_marble, blue_marble])

if min_depth != float('inf'):
    print(min_depth)
else:
    print(-1)



    


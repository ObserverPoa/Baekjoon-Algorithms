'''
각 영역을 탐색해서 양과 늑대의 개수를 구하고,
어느쪽이 잡아먹혔는지 판단해서 최종 카운팅에 더한다.
'''
import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

input = sys.stdin.readline

R, C = map(int, input().split())

grid = [
    [char for char in input().strip()]
    for _ in range(R)
]

def in_grid(x, y):
    return 0 <= x < R and 0 <= y < C

# 위쪽부터 시계방향 순 (x: 행, y: 열)
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

visited = set()

def dfs(x, y, counter):
    coord = (x, y)
    # 이미 방문했거나, 그리드 밖이거나, 울타리인 경우 리턴
    if coord in visited or not in_grid(x, y) or grid[x][y] == '#':
        return 
    
    # 방문 및 카운팅 처리
    visited.add(coord)
    counter[grid[x][y]] += 1

    # 4방향 탐색
    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        dfs(next_x, next_y, counter)


sheep_count = 0
wolf_count = 0

for x in range(R):
    for y in range(C):
        counter = defaultdict(int)
        dfs(x, y, counter)

        if counter['k'] > counter['v']:
            sheep_count += counter['k']
        else:
            wolf_count += counter['v']

print(f'{sheep_count} {wolf_count}')
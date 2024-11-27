'''
바이러스를 놓을 수 있는 칸의 개수는 10이하이기 때문에, 모든 조합을 검사할 수 있다.
'''
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

startable_coords = [] # 바이러스를 놓을 수 있는 모든 좌표
empty_count = 0 # 벽이 아닌 칸 개수
for x in range(N):
    for y in range(N):
        if grid[x][y] == 2:
            startable_coords.append((x, y))
        if grid[x][y] != 1:
            empty_count += 1

min_seconds = -1 # 최소 바이러스 장악 시간

for start_coords in combinations(startable_coords, M):
    leaf_coords = list(start_coords)
    visited = set(leaf_coords)
    seconds = -1 # 장악하는데 걸린 시간

    while leaf_coords:
        seconds += 1
        next_leaf_coords = []
        
        for x, y in leaf_coords:
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                next_coord = (nx, ny)
                if not (0 <= nx < N and 0 <= ny < N): continue # 격자 내 인가
                if grid[nx][ny] == 1: continue # 벽이 아닌가
                if next_coord in visited: continue # 방문하지 않았는가

                visited.add(next_coord)
                next_leaf_coords.append(next_coord)

        leaf_coords = next_leaf_coords
        
    
    if len(visited) == empty_count: # 벽이 아닌 칸을 모두 방문했는지
        if min_seconds == -1 or seconds < min_seconds:
            min_seconds = seconds # 최소 시간 갱신

print(min_seconds)
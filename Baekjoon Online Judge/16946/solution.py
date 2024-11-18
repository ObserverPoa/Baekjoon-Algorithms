import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [
    list(map(int, input().strip())) 
    for _ in range(N)
]

def in_grid(x, y):
    return 0 <= x < N and 0 <= y < M

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

group_id_by_coord = defaultdict(int) # key: 빈 공간의 좌표, value: 연결된 빈 공간끼리 묶은 그룹의 id
group_size_by_id = defaultdict(int) # key: 연결된 빈 공간끼리 묶은 그룹의 id, value: 그룹의 크기

# start_coord와 연결된 빈 공간들을 같은 그룹 id로 설정하고, 해당 그룹의 크기를 구하는 함수
def bfs(start_coord, group_id):
    queue = deque([start_coord])
    group_id_by_coord[start_coord] = group_id
    group_size_by_id[group_id] += 1

    while(queue):
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            next_coord = (nx, ny)
            if not in_grid(nx, ny): continue
            if grid[nx][ny] == 1: continue
            if group_id_by_coord[next_coord] > 0: continue

            group_id_by_coord[next_coord] = group_id
            group_size_by_id[group_id] += 1

            queue.append(next_coord)


# 모든 그룹 및 그룹의 크기를 구한다.
next_group_id = 1
for x in range(N):
    for y in range(M):
        coord = (x, y)
        if grid[x][y] == 1: continue
        if group_id_by_coord[coord] > 0: continue

        bfs(coord, next_group_id)
        next_group_id += 1

# 빈 공간일 경우 0을 출력하고,
# 벽일 경우 인접한 그룹들의 크기의 합에 1을 더하고 10으로 나눈 나머지를 출력한다.
for x in range(N):
    for y in range(M):
        coord = (x, y)
        if grid[x][y] == 0: 
            print(0, end="")
            continue
        
        group_ids = set()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_grid(nx, ny): continue
            if grid[nx][ny] == 1: continue
            
            group_ids.add(group_id_by_coord[(nx, ny)])
        
        moveable_count = 1
        for group_id in group_ids:
            moveable_count += group_size_by_id[group_id]
        
        print(moveable_count % 10, end="")
    print()
            
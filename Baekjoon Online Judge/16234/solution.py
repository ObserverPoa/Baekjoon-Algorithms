import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())

grid = [ list(map(int, input().split())) for _ in range(N) ]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# start 좌표가 속한 연합에 속한 좌표들을 반환하는 함수
def bfs(start, global_visited):
    queue = deque([start])
    visited = set([start]) # 연합국 목록
    total_count = 0 # 연합의 인구수

    while queue:
        x, y = queue.popleft()
        total_count += grid[x][y]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not (0 <= nx < N and 0 <= ny < N): continue # 유효한 좌표인가
            if (nx, ny) in global_visited: continue # 다른 연합에 속한 좌표인가
            if (nx, ny) in visited: continue # 방문하지 않은 좌표인가
            if not (L <= abs(grid[x][y] - grid[nx][ny]) <= R): continue # 연합 가능한가

            visited.add((nx, ny))
            queue.append((nx, ny))

    # 현재 연합 내의 인구 이동 처리
    average_count = total_count // len(visited)
    for x, y in visited:
        grid[x][y] = average_count
    
    return visited


days = 0
while True:
    visited = set()
    did_move = False # 오늘 인구 이동이 있었는가

    for x in range(N):
        for y in range(N):
            if (x, y) in visited:
                continue
            
            local_visited = bfs((x, y), visited)
            visited.update(local_visited)

            # 오늘 연합의 크기가 2 이상인 것이 존재했다면 인구 이동이 있었다는 뜻이다.
            if len(local_visited) > 1:
                did_move = True 
    
    if not did_move:
        break

    days += 1

print(days)

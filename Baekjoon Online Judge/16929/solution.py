import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [ 
    [char for char in input().strip()] 
    for _ in range(N) 
] 

def in_grid(x, y):
    return 0 <= x < N and 0 <= y < M

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# 같은 색깔로 이루어진 부분 그래프에 사이클이 있는지 확인하는 함수
def dfs(x, y, visited, prev):
    visited.add((x, y))

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if not in_grid(nx, ny): continue # 격자 내 인지 확인
        if grid[x][y] != grid[nx][ny]: continue # 같은 색깔로 이루어진 부분 그래프 내 인지 확인
        if (nx, ny) == prev: continue # 직전 방문 좌표가 아닌지 확인
        
        # 직전 방문 좌표를 제외하고, 방문했던 좌표에 도달할 수 있다면 사이클이 존재하는 것이다.
        if (nx, ny) in visited: 
            return True
        
        has_cycle = dfs(nx, ny, visited, (x, y))
        if has_cycle:
            return True

    return False

def is_cycle_exist():
    visited = set()

    for x in range(N):
        for y in range(M):
            if (x, y) in visited: 
                continue

            local_visited = set()
            has_cycle = dfs(x, y, local_visited, None)
            visited.update(local_visited)

            if has_cycle:
                return True

    return False


if is_cycle_exist():
    print('Yes')
else:
    print('No')

'''
(0, 0)에서 모든 경로에 대해 dfs를 하는데, 
이미 방문한 알파벳이 있을 경우 중단한다.
또한, 지금까지 같은 알파벳들을 방문해왔고, 같은 좌표에 있게 되는 경우가 여러가지 있을 수 있는데 
한번만 탐색하면 된다는 점이 중요하다. (key와 visited)
'''

import sys

input = sys.stdin.readline

R, C = map(int, input().split())

grid = [ [char for char in input().strip()] for _ in range(R) ]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

max_depth = 1

visited = set()

def dfs(x, y, path):
    global max_depth

    key = f'{x}_{y}_{sorted(path)}'
    if key in visited:
        return
    visited.add(key)

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if not (0 <= nx < R and 0 <= ny < C): continue
        if grid[nx][ny] in path: continue

        path.add(grid[nx][ny])
        max_depth = max(len(path), max_depth)
        dfs(nx, ny, path)
        path.remove(grid[nx][ny])

dfs(0, 0, set([grid[0][0]]))

print(max_depth)

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# grid의 둘레부분에서 벽이 아닌 모든 좌표들의 set 반환
def find_start_coords(h, w, grid):
    coords = set()
    
    for y in range(w):
        if grid[0][y] != '*':
            coords.add((0, y))
        if grid[h - 1][y] != '*':
            coords.add((h - 1, y))

    for x in range(h):
        if grid[x][0] != '*':
            coords.add((x, 0))
        if grid[x][w - 1] != '*':
            coords.add((x, w - 1))

    return coords

def solution(h, w, grid, keys):
    start_coords = find_start_coords(h, w, grid)
    queue = deque(start_coords)
    visited = [[False] * w for _ in range(h)]
    for x, y in start_coords:
        visited[x][y] = True
    
    locked_doors = defaultdict(list) # 열쇠를 얻기를 대기중인 문 좌표들
    document_count = 0

    while queue:
        x, y = queue.popleft()

        if grid[x][y] == '$':
            document_count += 1
        elif grid[x][y].isupper() and grid[x][y].lower() not in keys: # 문의 열쇠가 없는 경우
            locked_doors[grid[x][y]].append((x, y)) # 열쇠 대기 목록에 추가
            continue
        elif grid[x][y].islower() and grid[x][y] not in keys: # 새로운 열쇠를 얻었다면
            keys.add(grid[x][y])
            queue.extend(locked_doors[grid[x][y].upper()]) # 해당 키를 대기중이였던 문들의 좌표를 큐에 추가
            del locked_doors[grid[x][y].upper()] # 필수 아님

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < h and 0 <= ny < w): continue
            if grid[nx][ny] == '*': continue
            if visited[nx][ny]: continue

            visited[nx][ny] = True
            queue.append((nx, ny))
    
    return document_count


test_case_count = int(input())
for _ in range(test_case_count):
    h, w = map(int, input().split())
    grid = [ [char for char in input().strip()] for _ in range(h) ]
    keys = set(input().strip())

    print(solution(h, w, grid, keys))
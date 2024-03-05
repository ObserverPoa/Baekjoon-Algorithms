# https://www.acmicpc.net/problem/3197

import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

lake = [
    [cell for cell in sys.stdin.readline()]
    for _ in range(R)
]
    


dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def is_valid_coord(x, y):
    return 0 <= x < R and 0 <= y < C

def bfs(x, y, visited, near_ices, swans):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()

        if lake[x][y] == 'X':
            near_ices.add((x, y))
            continue
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))

        if lake[x][y] == 'L':
            swans.append((x, y))
        
        for dx, dy in zip(dxs, dys):
            if is_valid_coord(x + dx, y + dy):
                queue.append((x + dx, y + dy))


def solution():

    visited_global = set()
    next_melted_ices = set()
    main_area = None

    for x in range(R):
        for y in range(C):
            if lake[x][y] == 'X':
                continue
            elif (x, y) in visited_global:
                continue
            
            visited = set()
            near_ices = set()
            swans = []
            bfs(x, y, visited, near_ices, swans)
            visited_global.update(visited)
            next_melted_ices.update(near_ices)


            if len(swans) >= 2:
                return print(0)
            elif len(swans) == 1 and main_area is None:
                main_area = {
                    'waters': visited,
                    'near_ices': near_ices
                }
    
    if main_area is None or not next_melted_ices:
        return print(0)
    
    day = 1
    while len(next_melted_ices):
        melted_ices, next_melted_ices = next_melted_ices, set()
        for x, y in melted_ices:
            lake[x][y] = '.'
        for x, y in melted_ices:
            for dx, dy in zip(dxs, dys):
                if is_valid_coord(x + dx, y + dy) and lake[x + dx][y + dy] == 'X':
                    next_melted_ices.add((x + dx, y + dy))     
 
        near_ices = set()
        swans = []
        for x, y in main_area['near_ices']:
            bfs(x, y, main_area['waters'], near_ices, swans)
        main_area['near_ices'] = near_ices

        if len(swans):
            return print(day)
        day += 1
    

    print(day)

solution()
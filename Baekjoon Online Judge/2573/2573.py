# https://www.acmicpc.net/problem/2573

import sys
import collections

def solution():
    N, M = map(int, sys.stdin.readline().split())

    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]

    ices = {}

    for x in range(N):
        for y, height in enumerate(map(int, sys.stdin.readline().split())):
            if height > 0:
                ices[(x, y)] = (height, 0)
    
    for (x, y), (height, _) in ices.items():
        amount = 0
        for dx, dy in zip(dxs, dys):
            if (x + dx, y + dy) not in ices:
                amount += 1
        ices[(x, y)] = (height, amount)

    def bfs(coord, visited):
        queue = collections.deque([coord])
        visited.add(coord)
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in zip(dxs, dys):
                next = (x + dx, y + dy)
                if next in ices and next not in visited:
                    visited.add(next)
                    queue.append(next)
    years = 1

    while len(ices):
        removed_ice_coords = []

        for (x, y), (height, melt_amount) in ices.items():
            height -= melt_amount
            if height > 0:
                ices[(x, y)] = (height, melt_amount)
            else:
                removed_ice_coords.append((x, y))

        if len(ices) == len(removed_ice_coords):
            break
        
        is_bridge_removed = False # 2개 이상 인접한 얼음의 삭제 여부
        
        for x, y in removed_ice_coords:
            del ices[(x, y)]

            connection_count = 0
            for dx, dy in zip(dxs, dys):
                if (x + dx, y + dy) in ices:
                    connection_count += 1
                    height, melt_amount = ices[(x + dx, y + dy)]
                    ices[(x + dx, y + dy)] = (height, melt_amount + 1)
            if connection_count >= 2:
                is_bridge_removed = True

        if is_bridge_removed:
            visited = set()
            bfs(next(iter(ices)), visited)

            if len(visited) != len(ices):
                return print(years)

        years += 1

    print(0)
                      
solution()
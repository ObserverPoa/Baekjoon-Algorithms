'''
bfs를 해서 특정 칸으로 이동하는데 필요한 최소 움직임을 카운팅한다.
'''
import sys
from collections import deque

input = sys.stdin.readline

dxs = [1, 2, 2, 1, -1, -2, -2, -1]
dys = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(N, start, end):
    def in_board(x, y):
        return 0 <= x < N and 0 <= y < N
    
    visited = set([start])
    queue = deque([(start, 0)])

    while queue:
        coord, moves = queue.popleft()
        if coord == end:
            return moves
        
        x, y = coord
        for dx, dy in zip(dxs, dys):
            next = x + dx, y + dy
            if in_board(*next) and next not in visited:
                visited.add(next)
                queue.append((next, moves + 1))

T = int(input())

for _ in range(T):
    L = int(input())
    start = tuple(map(int, input().split()))
    target = tuple(map(int, input().split()))

    print(bfs(L, start, target))
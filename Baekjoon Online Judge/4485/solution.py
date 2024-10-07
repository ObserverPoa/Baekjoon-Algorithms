'''
각 테스트케이스마다 다익스트라 알고리즘을 통해 (0, 0)에서 모든 좌표로 가는 최소 비용을 구한다.
'''
import sys
import  heapq

input = sys.stdin.readline

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def in_cave(x, y, n):
    return 0 <= x < n and 0 <= y < n

# 다익스트라 알고리즘
def find_min_loss(cave):
    n = len(cave)
    pq = [(cave[0][0], 0, 0)]
    min_losses = [[float('inf') for _ in range(n)] for _ in range(n)]  
    min_losses[0][0] = cave[0][0]  

    while pq:
        losses, x, y = heapq.heappop(pq)
        if losses > min_losses[x][y]:
            continue
        
        for dx, dy in zip(dxs, dys):
            if not in_cave(x + dx, y + dy, n): continue

            new_losses = losses + cave[x + dx][y + dy]
            if new_losses < min_losses[x + dx][y + dy]:
                min_losses[x + dx][y + dy] = new_losses
                heapq.heappush(pq, (new_losses, x + dx, y + dy))

    return min_losses[-1][-1]

problem_num = 1
while True:
    N = int(input())
    if N == 0: break

    cave = [list(map(int, input().split())) for _ in range(N)]
    min_loss = find_min_loss(cave)
    print(f'Problem {problem_num}: {min_loss}')
    problem_num += 1

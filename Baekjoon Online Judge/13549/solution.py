'''
매번 현재 좌표에 2의 i제곱을 곱한 좌표들의 +-1 좌표들을 1초뒤에 방문하는 bfs를 수행한다.
'''
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())


def bfs(start, end):
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        num, seconds = queue.popleft()
        
        i = 0
        while num * (2 ** i) < 200000: # 현재 숫자에서 2를 계속 곱한 좌표는 즉시 이동 가능하다.
            portal = num * (2 ** i)
            visited.add(portal)
            if portal == end:
                return seconds

            for next in (portal + 1, portal - 1):
                if next not in visited and 0 <= next < 200000:
                    visited.add(next)
                    queue.append((next, seconds + 1))
            
            if num == 0: # 0일 경우 발생하는 무한루프 방지
                break
            i += 1

print(bfs(N, K))
'''
탐색 범위를 매번 1/4씩 줄여가면서 
주어진 좌표를 찾고, 최종 오프셋을 출력한다.
'''
import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

offset = 0 # 현재 영역의 좌상단 좌표 방문 순서

for n in range(N, 0, -1):
    mid = 2 ** (n - 1)
    block_size = mid ** 2 # 1/4영역의 크기

    if r < mid and c >= mid: # 오른쪽 위
        offset += block_size
        c -= mid
    elif r >= mid and c < mid: # 왼쪽 아래
        offset += 2 * block_size
        r -= mid
    elif r >= mid and c >= mid: # 오른쪽 아래
        offset += 3 * block_size
        r -= mid
        c -= mid

print(offset)
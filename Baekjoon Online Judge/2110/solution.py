'''
이분탐색의 대상: 공유기 간 최소거리의 최댓값
'''
import sys

input = sys.stdin.readline

N, C = map(int, input().split())

coords = [int(input()) for _ in range(N)]
coords.sort()

def is_possible(min_distance):
    count = 1
    distance = 0
    for i in range(1, N):
        gap = coords[i] - coords[i - 1]
        if distance + gap >= min_distance:
            count += 1
            distance = 0
        else:
            distance += gap
    
    return count >= C

left = 1
right = coords[-1] - coords[0] + 1

while left < right:
    mid = (left + right) // 2

    if is_possible(mid):
        left = mid + 1
    else:
        right = mid

print(left - 1)


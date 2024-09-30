'''
시작점 보다 크거나 같은 점 중 가장 작은 점, 
끝점 보다 작거나 같은 점 중 가장 큰 점을 
빠르게 찾기 위해 이분탐색을 사용한다.
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

points = list(sorted(map(int, input().split())))

# 이분탐색으로 point와 같거나 가장 가까운 점을 찾는다.
def search_nearest(point, left, right):
    if left == right:
        return left
    
    mid = left + (right - left) // 2

    if point <= points[mid]:
        return search_nearest(point, left, mid)
    else:
        return search_nearest(point, mid + 1, right)

for _ in range(M):
    start, end = sorted(map(int, input().split()))

    # 선분이 점 목록의 범위와 전혀 겹치지 않는지 확인
    if start > points[-1] or end < points[0]:
        print(0)
        continue
    
    # 시작점 보다 크거나 같은 점 중 가장 작은 점의 좌표의 +-1 중 하나
    i = search_nearest(start, 0, N - 1) 

    # 끝점 보다 작거나 같은 점 중 가장 작은 점의 좌표의 +-1 중 하나
    j = search_nearest(end, 0, N - 1) 

    # 시작점 보다 크거나 같은 점 중 가장 작은 점의 좌표
    left = [idx for idx in range(max(0, i - 1), min(N, i + 2)) if start <= points[idx]][0]

    # 끝점 보다 작거나 같은 점 중 가장 작은 점의 좌표
    right = [idx for idx in range(max(0, j - 1), min(N, j + 2)) if end >= points[idx]][-1]

    print(right - left + 1)
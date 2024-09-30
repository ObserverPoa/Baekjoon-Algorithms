'''
한 개의 장애물이 있는 격자에서, 화재가 난 헛간과 호수 사이의 최단거리를 구하는 문제이다.
헛간, 호수가 일직선상에 있고, 그 사이에 바위가 있다면 좌표를 통해 계산한 최단거리에 2를 더하고,
그렇지 않다면 2를 더하지 않는다.
'''
import sys

input = sys.stdin.readline

N = 10

coords = {}

# 바위, 헛간, 호수의 좌표 저장
for i in range(N):
    row = input().strip()
    for j, char in enumerate(row):
        if char != '.':
            coords[char] = (i, j)

bx, by = coords['B']
lx, ly = coords['L']
rx, ry = coords['R']

row_gap = abs(bx - lx) - 1 # 헛간과 호수 사이의 행 개수
col_gap = abs(by - ly) - 1 # 헛간과 호수 사이의 열 개수

if bx == lx: # 헛간과 호수의 행이 같은 경우
    if bx == rx and min(by, ly) < ry < max(by, ly): # 돌이 일직선 경로상에 있는 경우
        print(col_gap + 2)
    else:
        print(col_gap)
elif by == ly: # 헛간과 호수의 열이 같은 경우
    if by == ry and min(bx, lx) < rx < max(bx, lx): # 돌이 일직선 경로상에 있는 경우
        print(row_gap + 2)
    else:
        print(row_gap)
else:
    print(row_gap + col_gap + 1) # 꼭짓점 소 한 마리 추가
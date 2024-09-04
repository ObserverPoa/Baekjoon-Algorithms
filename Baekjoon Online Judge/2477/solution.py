'''
참외밭의 넓이를 구해서 1m^2에 자라는 참외의 개수와 곱한다.
참외밭은 직사각형에서 한쪽 모서리가 직각으로 파인 형태를 갖는다.
그래서 참외밭의 넓이는 큰 직사각형의 면적에서 작은 직사각형의 면적을 뺴서 구한다.
큰 직사각형의 면적: 가로방향의 최대 거리, 세로방향의 최대 거리를 곱한다.
작은 직사각형의 면적: 직각으로 파인 부분에서만 이동방향이 시계방향으로 변한다는 것을 이용해서 가로와 세로길이를 찾고, 곱한다.
'''

import sys

input = sys.stdin.readline

K = int(input())

# 반시계 방향 이동 경로 입력
paths = [
    list(map(int, input().split())) for _ in range(6)
]

# 시계방향 방향 전환 목록 정의
clockwise_directions = {
    1: 3, 4: 1, 2: 4, 3: 2
}

# 바깥 직사각형 면적 계산
def calc_outer_area():
    width, height = 1, 1
    for direction, length in paths:
        if direction in [1, 2]:
            width = max(length, width)
        else:
            height = max(length, height)
    return width * height

# 작은 직사각형(파인부분) 면적 계산
def calc_inner_area():
    for i, [direction, length] in enumerate(paths):
        prev_direction, prev_length = paths[i - 1]
        if clockwise_directions[prev_direction] == direction:
            return prev_length * length

area = calc_outer_area() - calc_inner_area()
print(K * area)

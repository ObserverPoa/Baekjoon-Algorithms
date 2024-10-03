'''
우측 하단 대각선의 숫자들이 제곱수라는 점을 이용한다.
대각선은 r과 c의 절대값이 같다. 이를 x라고 했을 때,
우측 하단 대각선부터 시계 방향 순으로, 대각선 위의 값들은 다음의 식으로 표현된다.
(2x + 1)^2
(2x + 1)^2 - 2x
(2x + 1)^2 - 4x
(2x + 1)^2 - 6x
대각선으로 나뉜 4개의 영역별로 좌표를 값으로 바꾸는 수식을 작성한다.
'''
import sys

input = sys.stdin.readline

def get_number(r, c):
    if r == c == 0:
        return 1
    
    if abs(r) > abs(c) or r == c:
        base = (2 * abs(r) + 1) ** 2
        offset = abs(r - c)
        if r > 0: # 우측 하단 대각선 + 하단 영역
            return base - offset
        else: # 좌측 상단 대각선 + 상단 영역
            return base - (4 * abs(r)) - offset
    else:
        base = (2 * abs(c) + 1) ** 2
        offset = abs(-c - r)
        if c > 0: # 우측 상단 대각선 + 우측 영역
            return base - (6 * abs(c)) - offset
        else: # 좌측 하단 대각선 + 좌측 영역
            return base - (2 * abs(c)) - offset


r1, c1, r2, c2 = map(int, input().split())

height = r2 - r1 + 1
width = c2 - c1 + 1
grid = [
    [0 for _ in range(width)]
    for _ in range(height)
] 

max_number_len = 0 # 가장 자리수가 긴 숫자

for x in range(height):
    for y in range(width):
        grid[x][y] = get_number(r1 + x, c1 + y)
        max_number_len = max(max_number_len, len(str(grid[x][y])))

for x in range(height):
    for y in range(width):
        spaces = ' ' * (max_number_len - len(str(grid[x][y])))
        print(spaces + str(grid[x][y]), end=" ")
    print()



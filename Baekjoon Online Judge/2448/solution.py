import sys
import math

input = sys.stdin.readline

N = int(input())
k = int(math.log2(N // 3))  # 자신을 복제해서 아래 줄을 생성하는 횟수

# 왼쪽 정렬된 상태로 계속 줄을 생성한다.
lines = [
    '*',
    '* *',
    '*****'
]

for _ in range(k):
    next_lines = []
    for line in lines:
        next_line = line
        next_line += ' ' * (len(lines[-1]) - len(line))
        next_line += ' '
        next_line += line
        next_lines.append(next_line)
    lines.extend(next_lines)

for i, line in enumerate(lines, 1):
    print(' ' * (len(lines) - i), end="") # 가운데 정렬을 위한 공백
    print(line, end="")
    print(' ' * (len(lines) - i)) # 출력형식이 잘못됬다고 나와서 추가


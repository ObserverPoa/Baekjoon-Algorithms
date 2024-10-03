'''
로봇청소기의 작동 규칙에 따라 구현한다.
drs와 dcs를 방향 전환 순서에 맞게 정의한다.
나머지 연산자 및 음수 인덱스 사용헤서 방향을 회전시킨다.
'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = [ list(map(int, input().split())) for _ in range(N) ]

# 북 동 남 서
drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

# 주변 4칸중 청소되지 않은 빈 칸의 존재 여부 반환
def is_near_dirty(r, c):
    for dr, dc in zip(drs, dcs):
        if room[r + dr][c + dc] == 0:
            return True
    return False

count = 0

while True:
    if room[r][c] == 0:
        room[r][c] = 2 # 청소된 칸
        count += 1

    if is_near_dirty(r, c):
        d = (d - 1) % 4
        if room[r + drs[d]][c + dcs[d]] == 0:
            r += drs[d]
            c += dcs[d]
    else:
        back = (d + 2) % 4
        if room[r + drs[back]][c + dcs[back]] != 1:
            r += drs[back]
            c += dcs[back]
        else:
            break

print(count)

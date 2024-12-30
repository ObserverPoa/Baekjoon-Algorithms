import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

array = [ list(map(int, input().split())) for _ in range(N) ]

# 바깥 레이어부터 안쪽 레이어까지 순회
for i in range(min(N, M) // 2):
    coords = [] # 시계방향으로 현재 레이어의 좌표들을 저장

    for y in range(i, M - i):
        coords.append((i, y))
    for x in range(i + 1, N - 1 - i):
        coords.append((x, M - 1 - i))
    for y in range(M - 1 - i, i - 1, -1):
        coords.append((N - 1 - i, y))
    for x in range(N - 2 - i, i, -1):
        coords.append((x, i))

    numbers = [array[x][y] for x, y in coords] # 회전하기 전의 현재 레이어의 값 백업
    
    # 백업한 값들을 회전 후의 배열 위치에 삽입
    offset = R % len(coords)
    for i in range(len(coords)):
        number = numbers[(i + offset) % len(coords)]
        x, y = coords[i]
        array[x][y] = number

for row in array:
    print(' '.join(map(str, row)))


    


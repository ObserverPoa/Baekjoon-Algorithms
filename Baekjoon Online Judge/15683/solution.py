import sys

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [ list(map(int, input().split())) for _ in range(N) ]

min_blind_spot_size = N * M

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# cctv 종류
cctv_directions = {
    1: [1, 0, 0, 0],
    2: [1, 0, 1, 0],
    3: [1, 1, 0, 0],
    4: [1, 1, 1, 0],
    5: [1, 1, 1, 1]
}

wall_count = 0 # 벽의 개수
cctvs = []
for x in range(N):
    for y in range(M):
        if grid[x][y] == 6:
            wall_count += 1
        elif grid[x][y] > 0:
            cctvs.append((x, y, grid[x][y]))

# 10진수를 4진수로 변경
def create_rotations(num):
    rotations = []
    while num >= 4:
        quotient, remainder = divmod(num, 4)
        num = quotient
        rotations.append(remainder)

    rotations.append(num)
    rotations.extend([0] * (len(cctvs) - len(rotations)))
    rotations.reverse()
    return rotations

# 모든 cctv에 대한 4방향 조합을 모두 검사한다.
for i in range(4 ** len(cctvs)):
    rotations = create_rotations(i)

    watched_coords = set() # 현재 조합에서 모든 cctv가 감시 가능한 좌표들

    for (x, y, cctv_kind), rotation in zip(cctvs, rotations):
        for dx, dy, i in zip(dxs, dys, range(rotation, rotation + 4)):
            # 현재 회전 상태에서 해당 방향을 볼 수 있는지 확인
            if not cctv_directions[cctv_kind][i % 4]: continue

            nx, ny = x, y
            distance = 0

            while 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 6:
                watched_coords.add((nx, ny))
                distance += 1
                nx, ny = x + (dx * distance), y + (dy * distance)
    
    blind_spot_size = N * M - wall_count - len(watched_coords)
    min_blind_spot_size = min(blind_spot_size, min_blind_spot_size)
        
print(min_blind_spot_size)

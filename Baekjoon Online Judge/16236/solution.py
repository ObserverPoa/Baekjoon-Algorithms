import sys

input = sys.stdin.readline

N = int(input())

area = [ list(map(int, input().split())) for _ in range(N) ]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
ㅎ
# 상어의 시작 좌표 얻고 해당위치 빈칸으로 설정
for x in range(N):
    for y in range(N):
        if area[x][y] == 9:
            shark_coord = (x, y)
            area[x][y] = 0

shark_size = 2 
current_eat_count = 0 # 현재 상어 크기에서 먹은 물고기 개수
total_seconds = 0

# 현재 상어 위치를 기준으로 먹어야 하는 물고기가 있다면 해당 물고기의 좌표와 거리 반환
def bfs():
    queue = [shark_coord]
    visited = [[False] * N for _ in range(N)]
    visited[shark_coord[0]][shark_coord[1]] = True
    distance = 1

    while queue:
        next_queue = []
        smaller_fishes = [] # 다음 인접 칸 중에서 먹을 수 있는 물고기 목록

        for x, y in queue:
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < N and 0 <= ny < N): continue
                if visited[nx][ny]: continue
                if shark_size < area[nx][ny]: continue

                visited[nx][ny] = True
                next_queue.append((nx, ny))

                if 0 < area[nx][ny] < shark_size:
                    smaller_fishes.append((nx, ny))

        # 먹을 수 있는 물고기가 있으면, 가장 위, 가장 좌측에 있는 물고기 정보를 반환
        smaller_fishes.sort()
        if smaller_fishes:
            return (*smaller_fishes[0], distance)

        queue = next_queue
        distance += 1

while True:
    ret = bfs()
    if ret is None:
        break

    x, y, distance = ret

    # 먹은 물고기 빈칸으로 설정하고, 상어 위치를 먹은 물고기로 이동
    area[x][y] = 0
    shark_coord = (x, y)

    total_seconds += distance

    # 상어 크기 증가 처리
    current_eat_count += 1
    if current_eat_count == shark_size:
        shark_size += 1
        current_eat_count = 0

print(total_seconds)
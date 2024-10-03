'''
치킨집의 개수는 최대 13개 이므로, 
M개의 치킨집을 남기는 모든 경우의 수에 대해 도시의 치킨 거리를 계산해서
도시의 치킨 거리의 최소값을 구한다. 
'''
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
city = [ list(map(int, input().split())) for _ in range(N) ]

chicken_coords = [] # 치킨집 좌표 목록
for x in range(N):
    for y in range(N):
        if city[x][y] == 2:
            chicken_coords.append((x, y))

chicken_distances_list = [] # 각 집과 모든 치킨집 사이의 거리 목록 [[(치킨집 좌표, 거리)]]
for x in range(N):
    for y in range(N):
        if city[x][y] == 1:
            chicken_distances = [
                ((cx, cy), abs(cx - x) + abs(cy - y)) for cx, cy in chicken_coords
            ]
            chicken_distances.sort(key=lambda x: x[1]) # 거리에 대해 오름차순 정렬
            chicken_distances_list.append(chicken_distances)

min_city_chicken_distance = 2 * N * 2 * N # 도시의 치킨 거리 최소값

# 치킨집 개수를 M개로 줄이는 모든 조합에 대해 도시의 치킨 거리 계산
for coords in combinations(chicken_coords, M):
    valid_chicken_coords = set(coords)
    city_chicken_distance = 0

    for chicken_distances in chicken_distances_list:
        for coord, distance in chicken_distances:
            if coord in valid_chicken_coords: 
                # 현재 조합에서 가장 가까운 치킨집 까지의 거리 더하기
                city_chicken_distance += distance
                break
    
    min_city_chicken_distance = min(min_city_chicken_distance, city_chicken_distance)

print(min_city_chicken_distance)

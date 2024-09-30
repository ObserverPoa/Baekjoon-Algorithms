'''
기존 인덱스와 함께 좌표값을 기준으로 오름차순으로 정렬하고,
앞에서부터 순회하면서 현재 좌표값보다 작은 좌표값들의 중복 없는 개수를 갱신하고, 
좌표 압축 결과를 쓴다.
'''
import sys

input = sys.stdin.readline

N = int(input())

coords = enumerate(map(int, input().split()))

compressed_coords = [0] * N # 좌표 압축 결과

unique_count = -1 # 서로 다른 좌표 Xj의 개수
max_coord = None # 서로 다른 좌표 Xj중 가장 큰 값

for i, coord in sorted(coords, key=lambda x: x[1]):
    if coord != max_coord:
        max_coord = coord
        unique_count += 1
    compressed_coords[i] = unique_count
        
print(' '.join(map(str, compressed_coords)))
'''
priority queue를 사용해서, 
매번 O(logn)의 시간복잡도로 가장 큰 거인의 키를 절반으로 만든다.
'''
import sys
import heapq

input = sys.stdin.readline

N, H, T = map(int, input().split())

# heapq는 min heap이므로, 음수로 키를 저장한다.
giant_heights = []
for _ in range(N):
    height = int(input())
    heapq.heappush(giant_heights, -height)

usage_count = 0
while usage_count < T:
    height = -heapq.heappop(giant_heights)
    if H > height:
        heapq.heappush(giant_heights, -height)
        break

    if height > 1:
        height //= 2

    usage_count += 1
    heapq.heappush(giant_heights, -height)


max_height = -heapq.heappop(giant_heights) # 최종적으로 가장 큰 거인의 키
if H > max_height:
    print('YES')
    print(usage_count)
else:
    print('NO')
    print(max_height)
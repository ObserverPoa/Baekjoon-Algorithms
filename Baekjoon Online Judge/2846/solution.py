import sys

input = sys.stdin.readline

N = int(input())

heights = list(map(int, input().split()))

max_size = 0
local_min_height = heights[0]
for i in range(1, len(heights)):
    if heights[i] <= heights[i - 1]:
        local_min_height = heights[i]
    else:
        max_size = max(heights[i] - local_min_height, max_size)

print(max_size)
# https://www.acmicpc.net/problem/14719

import sys

H, W = map(int, sys.stdin.readline().split())

heights = list(map(int, sys.stdin.readline().split()))

max_height = max(heights)

max_height_indicies = [
    i for i, height in enumerate(heights) if height == max_height
]

left_top = max_height_indicies[0]
right_top = max_height_indicies[-1]

water = 0

left = 0

for i in range(left, left_top + 1):
    if heights[i] >= heights[left]:
        if left + 1 < i:
            for j in range(left + 1, i):
                water += heights[left] - heights[j]
        left = i

right = len(heights) - 1

for i in range(right, right_top - 1, -1):
    if heights[i] >= heights[right]:
        if right - 1 > i:
            for j in range(i + 1, right):
                water += heights[right] - heights[j]
        right = i

for i in range(left_top + 1, right_top):
    water += max_height - heights[i]


print(water)
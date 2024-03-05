# https://www.acmicpc.net/problem/1655

import sys
import heapq

N = int(sys.stdin.readline())

smaller_nums, larger_nums = [], []
median = None

answers = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if median is None:
        median = num
        answers.append(median)
        continue
    
    if num >= median:
        heapq.heappush(larger_nums, num)
    else:
        heapq.heappush(smaller_nums, num * -1)
    
    if len(smaller_nums) > len(larger_nums):
        heapq.heappush(larger_nums, median)
        median = heapq.heappop(smaller_nums) * -1
    elif len(larger_nums) > len(smaller_nums) + 1:
        heapq.heappush(smaller_nums, median * -1)
        median = heapq.heappop(larger_nums)

    answers.append(median)


for answer in answers:
    print(answer)

'''
중앙값 보다 작은 값들은 최대 우선순위 큐에, 큰 값들은 최소 우선순위 큐에 저장한다.
'''
import sys
import heapq

input = sys.stdin.readline

N = int(input())

smaller_nums, larger_nums = [], []

median = int(input()) # 중앙값
answers = [median]

for _ in range(N - 1):
    num = int(input())
    
    # 중앙값과 비교해서 올바른 우선순위 큐에 넣는다.
    # 중앙값과 같으면 둘 중 어디에 넣어도 상관 없다.
    if num >= median:
        heapq.heappush(larger_nums, num)
    else:
        heapq.heappush(smaller_nums, -num)
    
    # larger_nums의 길이가 smaller_nums의 길이와 같거나 1 더 크도록 조정한다.
    if len(smaller_nums) > len(larger_nums):
        heapq.heappush(larger_nums, median)
        median = -heapq.heappop(smaller_nums)
    elif len(larger_nums) > len(smaller_nums) + 1:
        heapq.heappush(smaller_nums, -median)
        median = heapq.heappop(larger_nums)

    answers.append(median)

for answer in answers:
    print(answer)

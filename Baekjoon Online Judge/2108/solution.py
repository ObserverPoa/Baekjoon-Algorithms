'''
주어진 정수들에 대한 네 가지 기본 통계값들을 구한다
'''
import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

numbers = [int(input()) for _ in range(N)]
numbers.sort()

print(round(sum(numbers) / N)) # 산술평균
print(numbers[N // 2]) # 중앙값

# 최빈값 중 두 번째로 작은 값
counter = Counter(numbers)
number_counts = counter.most_common()
number_counts.sort(key=lambda x: (-x[1], x[0]))

if len(number_counts) >= 2 and number_counts[0][1] == number_counts[1][1]:
    print(number_counts[1][0])
else:
    print(number_counts[0][0])

print(max(numbers) - min(numbers)) # 범위
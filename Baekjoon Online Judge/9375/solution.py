'''
각 의상 그룹에서 0개 또는 1개의 의상을 선택하는 조합의 개수를 구한다.
'''
import sys
from functools import reduce
from collections import defaultdict

input = sys.stdin.readline

test_count = int(input())

for _ in range(test_count):
    N = int(input())

    counter = defaultdict(int)
    for _ in range(N):
        _, category = input().strip().split()
        counter[category] += 1

    # 각 그룹에서 옷을 선택하지 않거나 한개만 선택하는 경우의 수를 모두 곱한다.
    case_count = reduce(lambda acc, count: acc * (count + 1), counter.values(), 1)

    print(case_count - 1) # 아무것도 입지 않는 경우 제외
    

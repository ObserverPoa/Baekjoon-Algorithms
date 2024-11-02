'''
길이 N 수열의 모든 부분 수열의 개수는 2^N 이다. (수열의 각 항목을 선택하거나 말거나)
2^20은 약 100만으로, 완전탐색이 가능하다.
'''
import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = list(map(int, input().split()))

sequence_sums = [] # 부분수열의 합 목록
for i in range(1, N + 1):
    for sequence in combinations(S, i):
        sequence_sums.append(sum(sequence))


min_num = 1 # 부분수열의 합이 아닌 최소 자연수

# 부분수열의 합들을 오름차순으로 정렬하고 
# 이전 원소와 같거나 1 더 클때까지 순회한다.
for sequence_sum in sorted(sequence_sums):
    if min_num < sequence_sum:
        break
    min_num = sequence_sum + 1

print(min_num)

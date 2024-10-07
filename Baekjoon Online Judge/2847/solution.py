'''
점수를 감소시킬수만 있기 때문에, 마지막 레벨의 점수는 그대로 두고, 
레벨을 역순으로 순회하면서 이전 레벨의 점수보다 1작게 하기 위해 내려야 하는 양들을 더한다.
'''
import sys

input = sys.stdin.readline

N = int(input())

scores = [int(input()) for _ in range(N)]

total_decrease_count = 0 

for i in range(N - 2, -1, -1):
    if scores[i] >= scores[i + 1]: 
        decrease_count = scores[i] - scores[i + 1] + 1
        scores[i] -= decrease_count
        total_decrease_count += decrease_count

print(total_decrease_count)
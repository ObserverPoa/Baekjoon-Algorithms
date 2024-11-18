'''
2이상끼리 큰 숫자부터 묶어서 곱하고 더한다.
1이상 ~ 위에서 묶고 남은 한개는 그냥 더한다.

-1이하끼리 작은 숫자부터 묶어서 곱하고 더한다.
위에서 남은 한개는 그냥 더한다.
'''
import sys

input = sys.stdin.readline

N = int(input())

total_sum = 0
positives = [] # 2 이상 정수
negatives = [] # 0 이하 정수

for _ in range(N):
    num = int(input())
    if num >= 2:
        positives.append(num)
    elif num == 1:
        total_sum += 1
    else:
        negatives.append(num)


positives.sort(reverse=True)

if len(positives) % 2 == 1:
    total_sum += positives.pop()

for i in range(0, len(positives), 2):
    total_sum += positives[i] * positives[i + 1]


negatives.sort()

if len(negatives) % 2 == 1:
    total_sum += negatives.pop()

for i in range(0, len(negatives), 2):
    total_sum += negatives[i] * negatives[i + 1]

print(total_sum)


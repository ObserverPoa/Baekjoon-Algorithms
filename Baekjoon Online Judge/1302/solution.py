'''
책 이름별로 카운팅하고, 가장 많이 팔렸고 사전순으로 사장 앞선 책의 제목을 출력한다.
'''
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

counter = defaultdict(int)

for _ in range(N):
    counter[input().strip()] += 1

# 카운트에 대해 내림차순, 이름에 대해 오름차순으로 정렬했을때의 첫번째 책의 이름을 출력한다.
best_seller = sorted(counter.items(), key=lambda item: (-item[1], item[0]))[0]
print(best_seller[0])

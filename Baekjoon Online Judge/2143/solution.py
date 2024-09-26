import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
input()
A = list(map(int, input().split()))
input()
B = list(map(int, input().split()))

# A의 부배열 합 별 개수 카운팅
a_counter = defaultdict(int) 
for i in range(len(A)):
    sub_sum = 0
    for j in range(i, len(A)):
        sub_sum += A[j]
        a_counter[sub_sum] += 1

# B의 각 부배열 합과 더해서 T가 되는 A의 부배열 합이 있다면 그 개수를 더한다.
answer = 0
for i in range(len(B)):
    sub_sum = 0
    for j in range(i, len(B)):
        sub_sum += B[j]
        answer += a_counter[T - sub_sum] 

print(answer)
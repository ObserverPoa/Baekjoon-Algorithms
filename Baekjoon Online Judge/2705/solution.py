'''
팰린드롬은 대칭이기 떄문에, 한쪽 부분을 분할하는 경우의 수만 고려하면 된다.
재귀적으로 n을 2a+b 의 형태로 나눈다. a는 양쪽에 오는 숫자, b는 중앙의 숫자이다.
a만 계속 1이 될때까지 재귀적으로 분할한다.
b도 분할하면 중복이 발생하기 때문이다.
'''
import sys

input = sys.stdin.readline

T = int(input())

memo = [0] * 1001

# n의 팰린드롬 파티션 개수를 세는 함수
def partition(n):
    if memo[n]:
        return memo[n]
    elif n == 1:
        return 1

    count = 1

    # 각 단계에서 a의 최대값은 n의 절반 이하이다.
    for i in range(1, (n // 2) + 1):
        count += partition(i)

    memo[n] = count
    return count

for _ in range(T):
    n = int(input())
    print(partition(n))



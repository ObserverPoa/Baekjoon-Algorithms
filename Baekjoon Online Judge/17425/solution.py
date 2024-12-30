'''
1~100만 까지의 g(x) 를 미리 계산해둔다. 
1~100만 까지의 각각의 약수의 합을 구하는 시간복잡도는 약 O(NlogN)이라고 한다.

매번 g(x)를 계산하면, 시간복잡도는 총 O(T√N) 인데, 약 1억번이라서 시간초과 발생
'''
import sys

input = sys.stdin.readline

MAX_N = 10 ** 6

divisor_sums = [0] * (MAX_N + 1) # f[A]

for i in range(1, MAX_N + 1):
    for multiple in range(i, MAX_N + 1, i):
        divisor_sums[multiple] += i

g = [0] * (MAX_N + 1) # g[x]
for i in range(1, MAX_N + 1):
    g[i] = g[i - 1] + divisor_sums[i]


T = int(input())

for _ in range(T):
    n = int(input())
        
    print(g[n])
     

#############

def sum_range(left, right):
    return (right - left + 1) * (left + right) // 2

# O(√N)에 g(x) 계산
def func_g(n):
    total_sum = 0
    i = 1

    while True:
        max_divisor = n // i
        if max_divisor < i:
            break

        total_sum += i * (max_divisor - i + 1)

        if max_divisor >= i + 1:
            total_sum += sum_range(i + 1, max_divisor)

        i += 1

    return total_sum
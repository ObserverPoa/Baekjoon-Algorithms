import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def count_factors(n, factor):
    count = 0
    while n > 0:
        n //= factor
        count += n
    return count

twos = count_factors(n, 2) - count_factors(m, 2) - count_factors(n - m, 2)
fives = count_factors(n, 5) - count_factors(m, 5) - count_factors(n - m, 5)

print(min(twos, fives))
import sys

input = sys.stdin.readline

# 에라토스테네스의 체
is_primes = [True] * 1000001

for i in range(2, 1001):
    if not is_primes[i]: 
        continue
    j = i * 2
    while j <= 1000000:
        is_primes[j] = False
        j += i

primes = [i for i in range(1000001) if is_primes[i] and i >= 3]


# b-a가 가장 큰 것을 출력해야 하므로, 가장 작은 소수부터 n // 2 이하의 소수까지 검사해나간다.
while True:
    n = int(input())
    if n == 0: 
        break
    
    i = 0
    while primes[i] <= n // 2 and not is_primes[n - primes[i]]:
        i += 1
    
    if is_primes[n - primes[i]]:
        print(f'{n} = {primes[i]} + {n - primes[i]}')
    else:
        print("Goldbach's conjecture is wrong.")



n, k = map(int, input().split())

def factorial(x):
    product = 1
    for i in range(1, x + 1):
        product *= i
    return product

answer = factorial(n) // (factorial(n - k) * factorial(k))

print(answer % 10007)
number, power, denominator = map(int, input().split())

remaining = 1

while power >= 2:
    if number < denominator:
        if power % 2 == 1:
            remaining *= number % denominator
        number = number ** 2
        power //= 2
    else:
        number %= denominator

print((number * remaining) % denominator)





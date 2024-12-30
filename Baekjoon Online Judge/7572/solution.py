N = int(input())

year = N - 4

print(f'{"ABCDEFGHIJKL"[year % 12]}{"0123456789"[year % 10]}')
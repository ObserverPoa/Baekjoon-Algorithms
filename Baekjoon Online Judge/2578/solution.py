import sys

input = sys.stdin.readline

N = 5

grid = [
    list(map(int, input().split())) 
    for _ in range(N)
]

numbers = []
for _ in range(N):
    numbers.extend(map(int, input().split()))

def remove_number(num):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == num:
                grid[i][j] = 0
                return

def is_bingo():
    line_count = 0
    for i in range(N):
        if not any(grid[i]):
            line_count += 1
        if not any([grid[j][i] for j in range(N)]):
            line_count += 1

    if not any([grid[i][i] for i in range(N)]):
        line_count += 1
    if not any([grid[i][N - 1 - i] for i in range(N)]):
        line_count += 1
    
    return line_count >= 3
        

for i, number in enumerate(numbers, 1):
    remove_number(number)
    if is_bingo():
        print(i)
        break
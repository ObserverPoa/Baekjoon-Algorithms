import sys

input = sys.stdin.readline

N = int(input())

cols = [False] * N
right_left_diag = [False] * (2 * N - 1)
left_right_diag = [False] * (2 * N - 1)

def dfs(row):
    if row == N:
        return 1
    
    count = 0
    for col in range(N):
        if not cols[col] and not right_left_diag[row + col] and not left_right_diag[row - col + (N - 1)]:
            cols[col] = right_left_diag[row + col] = left_right_diag[row - col + (N - 1)] = True
            count += dfs(row + 1)
            cols[col] = right_left_diag[row + col] = left_right_diag[row - col + (N - 1)] = False
    return count

print(dfs(0))
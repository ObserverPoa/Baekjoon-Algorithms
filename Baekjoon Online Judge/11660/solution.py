import sys

input = sys.stdin.readline

N, M = map(int, input().split())

table = [ list(map(int, input().split())) for _ in range(N) ]

cumulative_sums = [[0] * N for _ in range(N)] # (0, 0)에서 (x, y)까지의 누적 합
for i in range(N):
    for j in range(N):
        cumulative_sums[i][j] += table[i][j] 
        if j > 0:
            cumulative_sums[i][j] += cumulative_sums[i][j - 1]

for i in range(1, N):
    for j in range(N):
        cumulative_sums[i][j] += cumulative_sums[i - 1][j]

for _ in range(M):
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())

    result = cumulative_sums[x2][y2]
    if x1 > 0:
        result -= cumulative_sums[x1 - 1][y2]
    if y1 > 0:
        result -= cumulative_sums[x2][y1 - 1]
    if x1 > 0 and y1 > 0:
        result += cumulative_sums[x1 - 1][y1 - 1]

    print(result)

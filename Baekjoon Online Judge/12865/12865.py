# https://www.acmicpc.net/problem/12865

import sys

N, K = map(int, sys.stdin.readline().split())

items = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(N)
]

dp = [
    [ 0 for _ in range(K + 1) ] 
    for _ in range(N + 1)
]

for i in range(1, N + 1):
    item_weight, item_value = items[i - 1]
    for j in range(1, K + 1):
        if item_weight <= j:
            dp[i][j] = max(dp[i- 1][j], dp[i - 1][j - item_weight] + item_value)
        else:
            dp[i][j] = dp[i- 1][j]

print(dp[N][K])
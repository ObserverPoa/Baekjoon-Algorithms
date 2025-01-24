import sys

input = sys.stdin.readline

N = int(input())

dp = [1] * 10
dp[0] = 0

for _ in range(N - 1):
    next_dp = [0] * 10
    for i in range(10):
        if i > 0:
            next_dp[i] += dp[i - 1]
        if i < 9:
            next_dp[i] += dp[i + 1]
    dp = next_dp

print(sum(dp) % 1_000_000_000)
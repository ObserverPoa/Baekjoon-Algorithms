'''
각 depth당 최대 21개의 노드만 탐색하면 되고, depth는 최대 약 100이므로
memo를 해서 dfs를 한다.
'''
import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

memo = {}

def dfs(value, idx):
    key = (value, idx)
    if key in memo:
        return memo[key]
    if not (0 <= value <= 20):
        return 0
    if idx == N - 1:
        if value == numbers[idx]:
            return 1
        else:
            return 0

    memo[key] = sum([
        dfs(value - numbers[idx], idx + 1),
        dfs(value + numbers[idx], idx + 1)
    ])

    return memo[key]

print(dfs(numbers[0], 1))
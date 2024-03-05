# https://www.acmicpc.net/problem/15649

import sys

n, m = map(int, sys.stdin.readline().split())

def dfs(sequence, nums):
    if len(sequence) >= m:
        print(' '.join(map(str, sequence)))
        return

    for i in range(len(nums)):
        sequence.append(nums[i])
        dfs(sequence, nums[:i] + nums[i + 1:])
        sequence.pop()

dfs([], list(range(1, n + 1)))

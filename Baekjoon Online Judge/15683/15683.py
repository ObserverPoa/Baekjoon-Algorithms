# https://www.acmicpc.net/problem/15683

import sys

n, m = map(int, sys.stdin.readline().split())

room = [
    [ cell for cell in map(int, sys.stdin.readline().split()) ]
    for _ in range(n)
]


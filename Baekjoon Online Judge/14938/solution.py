import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

item_counts = list(map(int, input().split()))

min_dists = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    min_dists[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    min_dists[a - 1][b - 1] = l
    min_dists[b - 1][a - 1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            if min_dists[i][j] > min_dists[i][k] + min_dists[k][j]:
                min_dists[i][j] = min_dists[i][k] + min_dists[k][j]

max_count = 0
for i in range(n):
    count = 0
    for j in range(n):
        if min_dists[i][j] <= m:
            count += item_counts[j]
    max_count = max(max_count, count)

print(max_count)

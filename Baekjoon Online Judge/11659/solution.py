import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

cumulative_sums = [numbers[0]]
for i in range(1, N):
    cumulative_sums.append(cumulative_sums[-1] + numbers[i])

for _ in range(M):
    i, j = map(lambda x: int(x) - 1, input().split())
    
    if i == 0:
        print(cumulative_sums[j])
    else:
        print(cumulative_sums[j] - cumulative_sums[i - 1])



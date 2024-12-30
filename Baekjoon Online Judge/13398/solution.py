import sys

input = sys.stdin.readline

n = int(input())

sequence = list(map(int, input().split()))


removed_max = sequence[0]
normal_max = sequence[0]

total_max = sequence[0]

for i in range(1, n):
    num = sequence[i]

    removed_max = max(removed_max + num, normal_max)
    normal_max = max(normal_max + num, num)

    total_max = max(removed_max, normal_max, total_max)

print(total_max)
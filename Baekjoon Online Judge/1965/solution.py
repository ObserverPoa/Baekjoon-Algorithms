'''
n이 1000 이하 이므로, O(n^2)이 가능하다. 매번 n크기의 리스트를 순회할 수 있다.
왼쪽부터 상자의 크기를 보고, 해당 크기에 담을 수 있는 상자의 최대 개수를 갱신해나간다.
해당 크기의 상자보다 작은 상자들은 다 담을 수 있는데, 그 중 가장 많은 상자를 담은 경우를 골라서 1 더해서 갱신한다.
'''
import sys

input = sys.stdin.readline

N = int(input())

box_sizes = list(map(int, input().split()))

max_counts = [0] * 1001 # 크기가 x인 상자에 담을 수 있는 최대 상자 개수 (자신 포함)

for size in box_sizes:
    max_counts[size] = max(max_counts[:size]) + 1

print(max(max_counts))



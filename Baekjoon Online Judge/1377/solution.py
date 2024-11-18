'''
1. 버블 소트의 각 루프에서:
각 숫자는 최대 한 칸씩 앞으로 이동할 수 있습니다.
한 번의 루프에서, 특정 숫자가 앞으로 이동하지 않는 경우도 있지만, 전체적으로 보면 한 번의 루프에서 최소 하나의 숫자는 이동합니다.

2. 정렬 전후 상태를 비교하면:
각 숫자가 정렬 전 위치에서 정렬 후 위치로 이동하는 "앞으로 이동 거리"를 계산할 수 있습니다.
최대 앞으로 이동 거리가 곧 정렬이 완료되기 위해 필요한 최소 루프 횟수를 나타냅니다.

3. 결론:
버블 소트는 항상 한 루프에서 최대 한 칸만 앞으로 이동할 수 있으므로, 최대 앞으로 이동 거리 + 1이 최소 루프 횟수가 됩니다.
'''
import sys

input = sys.stdin.readline

N = int(input())

array = [int(input()) for _ in range(N)]

max_front_moves = float('-inf')

for i, (j, _) in enumerate(sorted(enumerate(array), key=lambda x: x[1])):
    max_front_moves = max(j - i, max_front_moves)

# 마지막에 정렬되었음을 확인하는 루프 때문에 1을 더한다.
print(max_front_moves + 1)


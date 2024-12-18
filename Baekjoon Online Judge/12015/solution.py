'''
범위별 최대 수열 길이를 이진 탐색 트리에 저장한다. (세그먼트 트리)
자신보다 작은 숫자 중 최대 수열 길이를 O(logN)에 조회할 수 있고,
범위별 최대 수열 길이를 O(logN)에 갱신할 수 있다.
'''
import sys
from collections import deque
import math

input = sys.stdin.readline

N = int(input())

sequence = list(map(int, input().split()))

# 세그먼트 트리 초기화
min_num, max_num = min(sequence), max(sequence)
segment_tree = [None] * 2 ** (math.ceil(math.log2(max_num - min_num + 1)) + 1)
queue = deque([(min_num, max_num, 1)])
while queue:
    left, right, idx = queue.popleft()
    segment_tree[idx] = [left, right, 0]
    if left == right: 
        continue

    mid = (left + right) // 2
    queue.append((left, mid, idx * 2))
    queue.append((mid + 1, right, idx * 2 + 1))


# 자신보다 작은 숫자 중 최대 수열 길이 조회
def get_smaller_max_len(num):
    idx = 1
    max_len = 0 # num 미만의 숫자 중 최대 수열의 길이
    # 루트 노드에서서 리프 노드까지 내려간다
    while segment_tree[idx][0] != segment_tree[idx][1]:
        left_node = segment_tree[idx * 2]
        if num > left_node[1]:
            max_len = max(max_len, left_node[2]) # num보다 작은 값들의 최대 길이로 max_len 갱신
            idx = idx * 2 + 1
        else:
            idx = idx * 2
    return max_len


# 범위별 최대 수열 길이 갱신
def update_range_max_lens(num, max_len):
    idx = 1
    segment_tree[idx][2] = max(max_len, segment_tree[idx][2])

    # 루트 노드에서서 리프 노드까지 내려간다
    while segment_tree[idx][0] != segment_tree[idx][1]:
        left_node = segment_tree[idx * 2]
        if num > left_node[1]:
            idx = idx * 2 + 1
        else:
            idx = idx * 2
        segment_tree[idx][2] = max(max_len, segment_tree[idx][2])


for num in sequence:
    max_len = get_smaller_max_len(num) + 1
    update_range_max_lens(num, max_len)

print(segment_tree[1][2])



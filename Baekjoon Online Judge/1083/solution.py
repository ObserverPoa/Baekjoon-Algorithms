'''
최대 S번 인접한 원소끼리 교환 가능할 때, 배열을 최대한 내림차순 정렬한다.
앞에 있는 숫자일수록 전체의 사전 순서에 큰 영향을 끼치므로, 
앞에서부터 시작해서 교환 횟수를 최대한 소모하면서 뒤애서 가져올 수 있는 가장 큰 숫자를 앞으로 끌어올린다.
'''
import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

count = int(input()) # 최대 교환 횟수

for i in range(N):
    if count <= 0: # 교환 횟수를 모두 사용한 경우
        break

    max_num_idx = i # 끌어올릴 수 있는 가장 큰 숫자의 인덱스

    # 끌어올릴 수 있는 가장 큰 숫자를 찾는다.
    for j in range(i + 1, min(i + count + 1, N)):
        if nums[j] > nums[max_num_idx]:
            max_num_idx = j
    
    # 가능한 거리 내에 현재 숫자보다 더 큰 숫자가 있는 경우, 끌어올린다.
    if max_num_idx > i:
        count -= max_num_idx - i
        nums = nums[:i] + [nums[max_num_idx]] + nums[i:max_num_idx] + nums[max_num_idx + 1:]

print(' '.join(map(str, nums)))
        
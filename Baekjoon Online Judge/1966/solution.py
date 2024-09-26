'''
테스트케이스마다 시간복잡도는 대략 O(N^2) 이지만, 
N의 최대값이 100이므로, 문제 그대로 구현한다.
'''
import sys
from collections import deque

input = sys.stdin.readline

def find_order(priorities, target_index):
    queue = deque(enumerate(priorities)) # 초기 인덱스를 추가해서 queue 생성
    max_priority = max(map(lambda x: x[1], queue))
    order = 1

    while queue:
        index, priority = queue.popleft()
        if priority < max_priority: # 인쇄 불가능한 경우
            queue.append((index, priority))
            continue
        
        if index == target_index: # 대상 문서를 인쇄한 경우
            return order
        
        max_priority = max(map(lambda x: x[1], queue)) 
        order += 1

for _ in range(int(input())):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    print(find_order(priorities, M))
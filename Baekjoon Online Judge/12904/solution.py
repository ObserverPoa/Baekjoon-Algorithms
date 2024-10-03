'''
긴 문자열에서 조건에 따라 역으로 문자열을 한개씩 제거해간다.
맨 뒤에서 문자를 한개씩 제거하는 작업만 하므로, 매번 문자열을 뒤집지 않고, 
양방향 제거가 O(1)에 가능한 deque와 뒤집혔는지 여부를 판단하는 플래그를 사용한다.
'''
import sys
from collections import deque

input = sys.stdin.readline

S = input().strip()
T = input().strip()

is_reversed = False

queue = deque(T)

while len(queue) > len(S):
    back = queue.popleft() if is_reversed else queue.pop()

    if back == 'B':
        is_reversed = not is_reversed # 문자열 뒤집기 처리
    elif back != 'A':
        break

if is_reversed:
    queue.reverse()

if ''.join(queue) == S:
    print(1)
else:
    print(0)





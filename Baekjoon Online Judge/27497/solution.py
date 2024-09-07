'''
문자를 한개씩 앞 또는 뒤에 붙이거나 빼서
최종 문자열을 만들어야 하므로, deque를 사용한다.
또한, 마지막으로 추가된 문자를 제거할 수 있도록, 
추가할때마다 어느 위치에 추가했었는지에 대한 기록을 스택에 남긴다.
'''
import sys
from collections import deque

input = sys.stdin.readline

INSERT_BACK = '1'
INSERT_FRONT = '2'
REMOVE_LAST = '3'

N = int(input())

chars = deque()
histories = [] # 블록 추가 버튼을 누른 기록

for _ in range(N):
    params = input().strip().split()
    button = params[0]

    if button == INSERT_BACK:
        chars.append(params[1])
        histories.append(button)
    elif button == INSERT_FRONT:
        chars.appendleft(params[1])
        histories.append(button)
    elif button == REMOVE_LAST and histories:
        if histories.pop() == INSERT_BACK:
            chars.pop()
        else:
            chars.popleft()

result = ''.join(chars)
print(result if result else 0)

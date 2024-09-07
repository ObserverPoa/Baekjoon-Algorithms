'''
파이썬의 deque를 사용해서 명령에 따라 작업을 수행한다.
'''
import sys
import collections

input = sys.stdin.readline

N = int(input())

deque = collections.deque()

for _ in range(N):
    params = input().strip().split()
    operation = params[0]

    if operation == "push_front":
        deque.appendleft(int(params[1]))
    elif operation == "push_back":
        deque.append(int(params[1]))
    elif operation == "pop_front":
        print(deque.popleft() if deque else -1)
    elif operation == "pop_back":
        print(deque.pop() if deque else -1)
    elif operation == "size":
        print(len(deque))
    elif operation == "empty":
        print(1 if not deque else 0)
    elif operation == "front":
        print(deque[0] if deque else -1)
    elif operation == "back":
        print(deque[-1] if deque else -1)

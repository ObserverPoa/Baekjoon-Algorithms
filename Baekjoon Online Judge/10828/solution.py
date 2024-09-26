'''
리스트를 사용해서 명령에 따라 작동하는 스택을 구현한다.
'''
import sys

input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    args = input().split()

    if args[0] == 'push':
        stack.append(int(args[1]))
    elif args[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif args[0] == 'size':
        print(len(stack))
    elif args[0] == 'empty':
        print(0 if stack else 1)
    elif args[0] == 'top':
        print(stack[-1] if stack else -1)

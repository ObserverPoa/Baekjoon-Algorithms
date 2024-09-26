'''
리스트 한 개를 사용해서 풀이하면 시간 복잡도가 높다. (10만 x 50만)
커서의 위치에서만 삽입 및 삭제가 발생하기 때문에, 
2개의 스택을 사용해서 모든 명령을 O(1)으로 수행한다.
'''
import sys

input = sys.stdin.readline

# 커서 왼쪽과 오른쪽의 스택
left_stack = [ char for char in input().strip() ]
right_stack = []

M = int(input())

for _ in range(M):
    args = input().strip().split()
    command = args[0]

    if command == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command == 'B':
        if left_stack:
            left_stack.pop()
    elif command == 'P':
        left_stack.append(args[1])

# 오른쪽 스택은 문자들이 역순으로 들어있다.
print(''.join(left_stack) + ''.join(reversed(right_stack)))
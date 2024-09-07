'''
같은 종류의 괄호끼리 열리고 닫히는지 확인하기 위해서 스택을 사용한다.
'''
import sys

input = sys.stdin.readline

pairs = {
    '(': ')',
    '[': ']'
}

# 스택에 여는 괄호를 순서대로 넣는데, 스택의 맨 위 괄호의 닫는 괄호라면 스택에서 뺀다.
def is_balanced_string(string):
    stack = []
    for char in string:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if stack and pairs[stack[-1]] == char:
                stack.pop()
            else:
                # 닫는 괄호인데 스택이 비었거나 마지막으로 열린 괄호와 매칭되지 않으면
                return False 

    return not stack # 스택이 비었다면 균형잡힌 문자열이다.


while True:
    line = input().rstrip()
    if line == '.':
        break

    print('yes' if is_balanced_string(line) else 'no')
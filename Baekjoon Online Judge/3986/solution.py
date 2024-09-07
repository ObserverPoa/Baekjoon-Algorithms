'''
모든 글자를 선끼리 교차하지 않으면서 같은 글자끼리 짝지을 수 있다는 것은,
어떤 글자가 등장했때 그 글자가 다음에 한번 더 등장해야 하며, 
그 사이에 있는 글자들 끼리는 짝이 지어진 상태여야 한다.
'''
import sys

input = sys.stdin.readline

# 스택에 글자를 순서대로 넣는데, 스택의 맨 위 글자와 같다면 스택에서 뺀다.
def is_good_word(word):
    stack = []
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return not stack # 스택이 비었다면 좋은 단어이다.

N = int(input())

count = sum([
    1 for _ in range(N) if is_good_word(input().strip())
])

print(count)
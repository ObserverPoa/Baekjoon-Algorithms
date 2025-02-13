import sys
from collections import deque

input = sys.stdin.readline

S = input().strip()
T = input().strip()

def dfs(chars: deque, is_reversed):
    if len(chars) == len(S):
        text = ''.join(reversed(chars)) if is_reversed else ''.join(chars)
        return text == S
    
    front_idx = -1 if is_reversed else 0
    back_idx = 0 if is_reversed else -1

    if chars[front_idx] == 'B':
        chars.pop() if is_reversed else chars.popleft()
        if dfs(chars, not is_reversed):
            return True
        chars.append('B') if is_reversed else chars.appendleft('B')
    if chars[back_idx] == 'A':
        chars.popleft() if is_reversed else chars.pop()
        if dfs(chars, is_reversed):
            return True
        chars.appendleft('A') if is_reversed else chars.append('A')

    return False

if dfs(deque(T), False):
    print(1)
else:
    print(0)
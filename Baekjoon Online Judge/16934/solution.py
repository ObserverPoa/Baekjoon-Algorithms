import sys

input = sys.stdin.readline

class Node:
    def __init__(self):
        self.count = 0
        self.children = {}

root = Node()

def sign_up(nickname):
    node = root
    min_prefix_end_idx = None
    for i, char in enumerate(nickname):
        if char not in node.children:
            node.children[char] = Node()
            if min_prefix_end_idx is None:
                min_prefix_end_idx = i
        node = node.children[char]

    node.count += 1

    if min_prefix_end_idx is None:
        if node.count <= 1:
            return nickname
        else:
            return f'{nickname}{node.count}'
    else:
        return nickname[:min_prefix_end_idx + 1]

N = int(input())
for _ in range(N):
    nickname = input().strip()
    print(sign_up(nickname))
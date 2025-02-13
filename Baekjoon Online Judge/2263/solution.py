'''
이진 트리를 루트 노드부터 좌측 서브트리와 우측 서브트리 순서대로 재귀적으로 방문했을때,
좌측 서브트리를 방문완료한 순서가 인오더이고,
우측 서브트리까지 모두 방문완료한 순서가 포스트오더라고 할 수 있다.

인오더와 포스트오더를 사용해, 다음과 같이 트리 구조를 복원할 수 있다.
1. 기본적으로, 인오더를 순회하면서 나오는 노드는, 자신의 우측 서브트리의 루트에서 왼쪽으로 끝까지 한번 내려갔을때의 노드가 된다.
2. 단, 자신의 우측 서브트리를 이미 다 탐색했다면 (포스트오더에 자신의 노드가 나왔다면), 자신의 우측 상단방향 부모노드가 된다.
3. 즉, 포스트 오더를 순회하면서 나오는 노드는, 현재까지 순회한 인오더에서 이미 나온적이 있다면 해당 노드로 이동하고 해당 노드의 우측 서브트리 탐색을 완료한다.
'''
import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None

in_order.reverse()
post_order.reverse()

tree = defaultdict(Node)
stack = []
child = None

# in_order는 항상 post_order보다 먼저 소진된다.
while in_order or post_order:
    
    # 1번 및 2번 작업
    while in_order and (not stack or stack[-1] != post_order[-1]):
        node = in_order.pop()
        stack.append(node)
        
        if child is not None:
            tree[node].left = child
            tree[child].parent = node
        child = None
    
    # 3번 작업
    while post_order and stack and post_order[-1] == stack[-1]:
        node = post_order.pop()
        stack.pop()
        
        if child is not None:
            tree[node].right = child
            tree[child].parent = node
        child = node

# 루트 노드 찾기
root = 1
while tree[root].parent is not None:
    root = tree[root].parent

# 전위 탐색 결과 출력
def pre_order(node):
    if node is None:
        return
    
    print(node, end=" ")
    pre_order(tree[node].left)
    pre_order(tree[node].right)

pre_order(root)
print()
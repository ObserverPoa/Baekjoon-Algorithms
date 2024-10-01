'''
배열로 이진 트리를 만들고, 중위 순회를 해서 빌딩 번호를 채워넣는다.
'''
import sys

input = sys.stdin.readline

K = int(input())

building_nums = list(map(int, input().split()))
building_nums.reverse()

binary_tree = [0] * (2 ** K)

# 중위 순회
def dfs(idx):
    if idx >= len(binary_tree):
        return
    
    dfs(idx * 2)
    binary_tree[idx] = building_nums.pop()
    dfs(idx * 2 + 1)

dfs(1)

for i in range(K):
    for j in range(2 ** i, 2 ** (i + 1)):
        print(binary_tree[j], end=" ")
    print()

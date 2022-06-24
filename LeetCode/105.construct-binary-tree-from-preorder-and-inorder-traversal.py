#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root] # DFS stack
        j = 0 # inorder list index
        for i in range(1, len(preorder)):
            if stack[-1].val != inorder[j]: 
                # 왼쪽 자식으로의 탐색이 아직 끝나지 않은 것을 재현
                stack[-1].left = TreeNode(preorder[i])
                stack.append(stack[-1].left)
            else:
                # 왼쪽 자식으로의 탐색이 끝난 후, 우측 자식이 있을 때 까지 부모 노드로 되돌아가는 것을 재현
                while stack and stack[-1].val == inorder[j]: 
                    prev = stack.pop()
                    j += 1
                prev.right = TreeNode(preorder[i])
                stack.append(prev.right)


        return root
# @lc code=end


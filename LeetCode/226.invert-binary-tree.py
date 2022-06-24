#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 서브트리를 스왑하는 순서는 상관이 없다.
        # 어떤 방식으로든 모든 노드를 탐색하며 해당 노드의 서브트리를 서로 스왑해주면 그만이다.
        def invert(node):
            if node is None:
                return

            invert(node.left)
            invert(node.right)

            node.left, node.right = node.right, node.left
            return

        invert(root)
        return root
# @lc code=end


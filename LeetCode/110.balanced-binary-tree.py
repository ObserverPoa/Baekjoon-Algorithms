#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
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
    is_balanced: int = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return -1

            left_height = height(node.left)
            right_height = height(node.right)

            if abs(left_height - right_height) > 1:
                self.is_balanced = False
            
            return max(left_height, right_height) + 1

        height(root)
        return self.is_balanced

            
# @lc code=end


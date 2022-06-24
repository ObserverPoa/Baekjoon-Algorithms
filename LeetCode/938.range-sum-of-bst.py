#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
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
    range_sum: int = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            if root.val < low:
                self.rangeSumBST(root.right, low, high)
            elif root.val > high:
                self.rangeSumBST(root.left, low, high)
            else:
                self.range_sum += root.val
                if root.val > low:
                    self.rangeSumBST(root.left, low, high)
                if root.val < high:
                    self.rangeSumBST(root.right, low, high)
        return self.range_sum
                

# @lc code=end


#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    prev: int = -1
    min_distance: int = sys.maxsize

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node:
                dfs(node.left)
                if self.prev != -1:
                    self.min_distance = min(self.min_distance, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)
        dfs(root)
        return self.min_distance
# @lc code=end


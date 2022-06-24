#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
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
    longest: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            path_len = 0 # 현재 서브트리내의 최대 경로 길이
            height = 0 # 같은 수로 구성된 경로의 최대 높이

            # path_len과 height 업데이트.
            if node.left and node.left.val == node.val:
                path_len += left_height + 1
                height = max(height, left_height + 1)
            if node.right and node.right.val == node.val:
                path_len += right_height + 1
                height = max(height, right_height + 1)
            
            # longest 업데이트
            self.longest = max(self.longest, path_len)

            return height

        dfs(root)
        return self.longest
# @lc code=end


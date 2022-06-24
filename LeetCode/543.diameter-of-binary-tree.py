#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
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
    longest: int = 0 # 중첩함수인 dfs내에서 변수 재할당을 위해서 클래스 변수를 활용했다.

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node is None:
                return -1

            left_max = height(node.left) # 왼쪽 서브트리의 높이
            right_max = height(node.right) # 오른쪽 서브트리의 높이

            self.longest = max(self.longest, left_max + right_max + 2) # 최대 diameter 갱신
            
            return max(left_max, right_max) + 1 # 현재 서브트리의 높이
        
        height(root)
        return self.longest

# @lc code=end


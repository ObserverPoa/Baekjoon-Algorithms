#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS를 이용한 풀이
        # def dfs(node: Optional[TreeNode], depth: int, max_depth: int) -> None:
        #     if not node:
        #         return max(max_depth, depth)
        #     max_depth = dfs(node.left, depth + 1, max_depth)
        #     max_depth = dfs(node.right, depth + 1, max_depth)
        #     return max_depth
        
        # return dfs(root, 0, 0)

        # BFS를 이용한 풀이
        # BFS는 depth를 1씩 늘려가므로, len(q)를 이용해서 각 depth를 구분해가며 BFS를 진행한다.
        import collections

        if root is None:
            return 0

        q = collections.deque([root])

        max_depth = 0
        while q:
            max_depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        
        return max_depth



# @lc code=end


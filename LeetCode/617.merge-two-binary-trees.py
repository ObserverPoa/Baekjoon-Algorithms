#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not (root1 and root2):
            return root1 or root2

        # BFS로 탐색하며 tree1에 tree2를 합친다.
        q = collections.deque([(root1, root2)])
        
        while q:
            node1, node2 = q.popleft()

            node1.val += node2.val

            if node1.left and node2.left: # tree1, tree2 둘다 노드가 있으면 탐색을 계속한다.
                q.append((node1.left, node2.left))
            elif node1.left is None and node2.left: # tree1은 없는데 tree2는 있는 경우 tree1쪽에 tree2의 서브트리를 붙인다.
                node1.left = node2.left
            
            if node1.right and node2.right:
                q.append((node1.right, node2.right))
            elif node1.right is None and node2.right:
                node1.right = node2.right


        return root1



# @lc code=end


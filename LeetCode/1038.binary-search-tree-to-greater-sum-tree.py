#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, sum):
            if node is None:
                return sum # 리프노드에 도달하면 백트래킹을 하며 합을 더하기 위해 지금까지의 sum을 반환한다.
            
            node.val += dfs(node.right, sum) # 현재 노드보다 큰 노드들의 합을 더한다.
            left = dfs(node.left, node.val) # 현재 노드까지의 합을 좌측 서브트리에 전달하고, 현재 노드까지의 합(현재 노드 + 우측 서브트리) + 좌측 서브트리의 합을 반환받는다.

            return left # 현재 서브트리의 모든 값의 합을 반환한다.

        dfs(root, 0)
        return root
# @lc code=end


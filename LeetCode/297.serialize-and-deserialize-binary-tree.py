#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = collections.deque([root])
        values = []
        while q:
            node = q.popleft()

            if node:
                values.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                values.append('')
        
        return ','.join(values)        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        values = collections.deque(data.split(','))
        root = TreeNode(int(values.popleft()))
        q = collections.deque([root])

        while q:
            node = q.popleft()
            left_val, right_val = values.popleft(), values.popleft()

            if left_val:
                node.left = TreeNode(int(left_val))
                q.append(node.left)
            if right_val:
                node.right = TreeNode(int(right_val))
                q.append(node.right)

        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end


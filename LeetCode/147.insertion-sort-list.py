#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = cursor = ListNode()
            
        while head:
            while cursor.next and cursor.next.val < head.val:
                cursor = cursor.next
            
            cursor.next, head.next, head = head, cursor.next, head.next
            
            # 필요한 경우만 cursor를 맨앞으로 되돌린다.
            if head and cursor.next.val > head.val:
                cursor = root

        return root.next
# @lc code=end


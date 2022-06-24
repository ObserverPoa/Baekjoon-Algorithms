#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd_head = odd_tail = head
        even_head = even_tail = head.next

        node = head.next.next
        index = 1

        while node:
            if index % 2:
                odd_tail.next = odd_tail = node
            else:
                even_tail.next = even_tail = node
                
            node = node.next
            index += 1
        
        odd_tail.next = even_head
        even_tail.next = None

        return odd_head
# @lc code=end


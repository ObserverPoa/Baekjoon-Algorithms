#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 정렬해서 합치는 부분 재귀로 구현
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
                l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge sort 구현

        if head is None or head.next is None:
            return head
        
        # 리스트를 반으로 쪼개는 부분
        half = slow = fast = head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None
        
        # 재귀호출하는 부분
        first = self.sortList(head)
        second = self.sortList(slow)

        # 정렬해서 합치는 부분 (백트래킹)
        root = ListNode()
        node = root
        while first and second:
            if first.val < second.val:
                node.next = first
                first = first.next
            else:
                node.next = second
                second = second.next
            node = node.next
        node.next = first or second

        return root.next

# @lc code=end


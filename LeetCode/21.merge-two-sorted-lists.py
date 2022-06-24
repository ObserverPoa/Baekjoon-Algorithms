#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        root = node = ListNode()
        
        # 리스트 합치기 (각 loop에서의 list1과 list2 맨 앞의 노드 중 작은 노드를 반복해서 붙여감)
        while list1 and list2:
            if list1.val < list2.val:
                node.next, node, list1 = list1, list1, list1.next
            else:
                node.next, node, list2 = list2, list2, list2.next
        
        # list1또는 list2둘중에 남은 것이 있다면 붙여준다.
        if list1:
            node.next = list1
        elif list2:
            node.next = list2
        
        return root.next
# @lc code=end


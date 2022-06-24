#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0, head)
        prev = root
        first = root.next

        while first and first.next:
            second = first.next
            
            # 현재 pair의 이전 node의 next 변경
            prev.next = second 

            # 현재 pair내의 첫번째 노드의 next를 먼저 변경한 다음 두번째 노드의 next를 변경.
            # prev -> ( second -> first )
            first.next = second.next 
            second.next = first

            # prev가 현재 pair의 두번째 노드(first)를 가리키게 하고,
            # first가 현재 pair의 다음 노드를 가리키게 한다.
            prev = first
            first = first.next
        
        return root.next

# @lc code=end


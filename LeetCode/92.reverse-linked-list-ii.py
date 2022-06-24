#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = node = ListNode(0, head)

        for i in range(right + 1):
            if i == left - 1: # 뒤집는 범위 바로 이전의 노드를 저장 (prefix)
                prefix, node = node, node.next
            elif i == left: # 뒤집는 범위내에서 가장 위에 오게 될 노드 저장 (mid_tail)
                mid_tail, prev, node = node, node, node.next
            elif i > left and i < right: # 뒤집기
                node.next, node, prev = prev, node.next, node
            elif i == right: # 마지막으로 뒤집은 후, prefix와 mid_tail의 next를 지정해준다.
                prefix.next, mid_tail.next, node.next = node, node.next, prev
            else:
                node = node.next

        return root.next
# @lc code=end


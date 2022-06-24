#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
import heapq
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        root = node = ListNode()

        stack = [head for head in lists if head]
        stack.sort(key=lambda x: x.val, reverse=True)

        while stack:
            # 맨위에꺼 첫번째 노드 연결하기
            node.next = node = stack[-1]

            # 맨위에꺼 다음으로 이동시키기
            stack[-1] = stack[-1].next

            if stack[-1] is None: # 맨위에꺼 비어있을경우 pop
                stack.pop()
            else: # 맨위에꺼의 val이 갱신되었으므로 맨위의 것만 bubble sort
                for i in range(len(stack) - 2, -1, -1):
                    if stack[i + 1].val > stack[i].val:
                        stack[i], stack [i + 1] = stack[i + 1], stack[i]
                    else:
                        break

        return root.next

    


# @lc code=end


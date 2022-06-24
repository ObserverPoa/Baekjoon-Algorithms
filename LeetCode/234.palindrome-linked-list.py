#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # O(n) space
        # check = []
        
        # while head:
        #     check.append(head.val)
        #     head = head.next
        
        # return check == check[::-1]

        # O(1) space (런너 기법 사용)
        rev = None
        slow = fast = head

        # 2칸씩 이동하는 포인터가 끝에 도달했을 때, 1칸씩 이동하는 포인터는 리스트의 중앙에 도달해 있다.
        # 1칸씩 중앙으로 이동하면서, 각 노드를 수정하여 리스트의 앞 절반을 중앙에서 헤드로 향하는 역방향 리스트로 바꾸고, 그 리스트의 헤더는 rev가 된다.
        while fast and fast.next:
            fast = fast.next.next

            new_rev = slow
            slow = slow.next
            new_rev.next = rev
            rev = new_rev

        # 리스트 길이가 홀수일 경우 
        if fast: 
            slow = slow.next
        
        # 리스트의 중앙에서 양쪽으로 1칸씩 퍼져나가면서 값이 같은지 비교
        while rev and slow and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        
        return not rev and not slow # rev 와 slow둘다 끝에 도달했다면 True.


# @lc code=end


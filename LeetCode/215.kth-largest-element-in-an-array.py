#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # return sorted(nums, reverse=True)[k - 1]
        
        # heap을 이용한 풀이
        nums = list(map(lambda x: -x, nums))
        heapq.heapify(nums)
        for _ in range(k - 1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)
# @lc code=end


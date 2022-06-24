#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans, local_sum = nums[0], 0
        for num in nums:
            if local_sum > 0:
                local_sum += num
            else:
                local_sum = num
            ans = max(ans, local_sum)
        return ans
        
# @lc code=end


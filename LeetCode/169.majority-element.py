#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        if not nums:
            return None
        elif len(nums) == 1:
            return nums[0]

        mid_idx = len(nums) // 2

        left = self.majorityElement(nums[:mid_idx])
        right = self.majorityElement(nums[mid_idx:])

        return left if nums.count(left) > mid_idx else right
        
        
# @lc code=end


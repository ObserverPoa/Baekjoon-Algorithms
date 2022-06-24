#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # fastest solution
        # nums_map = {}
        # for i, num in enumerate(nums):
        #     if target - num in nums_map:
        #         return [nums_map[target-num], i]
        #     nums_map[num] = i

        # two pointer solution
        nums = list(enumerate(nums))
        nums.sort(key=lambda x: x[1])
        left, right = 0, len(nums) - 1

        while left != right:
            if nums[left][1] + nums[right][1] < target:
                left += 1
            elif nums[left][1] + nums[right][1] > target:
                right -= 1
            else:
                return [nums[left][0], nums[right][0]]


        
# @lc code=end

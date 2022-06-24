#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        unique_nums = []
        while len(unique_nums) < 2 and len(nums) > 0:
            test = nums.pop(0)
            try:
                nums.remove(test)
            except ValueError:
                unique_nums.append(test)
        return unique_nums
# @lc code=end


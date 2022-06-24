#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
import functools
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(x, y):
            return int(y + x) - int(x + y)

        nums = list(map(str, nums))
        nums.sort(key=functools.cmp_to_key(compare))
        
        if nums[0] == '0':
            return '0'
        else:
            return ''.join(nums)


# @lc code=end


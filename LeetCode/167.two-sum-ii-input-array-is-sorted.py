#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # binary search 풀이
        # for i, number in enumerate(numbers):
        #     j = bisect.bisect_left(numbers, target - number, i + 1)
        #     if j < len(numbers) and numbers[j] == target - number:
        #         return [i + 1, j + 1]


        # two pointer 풀이
        i, j = 0, len(numbers) - 1
        while i < j:
            cur_sum = numbers[i] + numbers[j]
            if cur_sum > target:
                j -= 1
            elif cur_sum < target:
                i += 1
            else:
                return [i + 1, j + 1]

# @lc code=end


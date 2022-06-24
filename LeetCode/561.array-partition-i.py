#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition I
#

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        # 정렬 후, 앞에서부터 차례로 두쌍씩 묶은다음 각 쌍의 왼쪽 값을 모두 더한것이 문제 조건에서의 최대 합이다.

        nums.sort()
        sum = 0
        for i in range(len(nums)):
            if not i % 2:
                sum += nums[i]
        return sum
# @lc code=end


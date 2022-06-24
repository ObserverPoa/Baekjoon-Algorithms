#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = []

        # 각 num의 좌측 누적 곱을 맨 왼쪽부터 오른쪽으로 이동하며 계산해서 answer에 저장한다.
        temp = 1
        for num in nums:
            answer.append(temp)
            temp *= num

        # 각 num의 우측 누적 곱을 맨 오른쪽부터 왼쪽으로 이동하며 answer의 각 값과 곱한다.
        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= temp
            temp *= nums[i]

        return answer


# @lc code=end


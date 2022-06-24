#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = left + (right - left) // 2
                if target < nums[mid]:
                    return binary_search(left, mid - 1)
                elif target > nums[mid]:
                    return binary_search(mid + 1, right)
                else:
                    return mid
            else:
                return -1
        
        front = 0 # rotate되기 이전 상태의 맨 앞 element의 index
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                front = i
                break
        nums = nums[front:] + nums[:front]

        idx = binary_search(0, len(nums) - 1)

        return (idx + front) % len(nums) if idx != -1 else -1


# @lc code=end


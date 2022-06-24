#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # return list(set(nums1).intersection(set(nums2)))

        intersection = set()

        nums1.sort()
        nums2.sort()

        while nums1 and nums2:
            if nums1[-1] > nums2[-1]:
                nums1.pop()
            elif nums1[-1] < nums2[-1]:
                nums2.pop()
            else:
                intersection.add(nums1.pop())
                nums2.pop()

        return intersection


# @lc code=end


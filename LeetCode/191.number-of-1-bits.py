#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n:
            if n & 1:
                weight += 1
            n = n >> 1
        return weight
# @lc code=end


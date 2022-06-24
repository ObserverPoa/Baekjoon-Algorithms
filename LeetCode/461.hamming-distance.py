#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        for bit in bin(x ^ y)[2:]:
            if bit == '1':
                distance += 1
        return distance
# @lc code=end


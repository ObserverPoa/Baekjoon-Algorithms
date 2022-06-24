#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1, 2]

        for i in range(2, n):
            ways.append(ways[i - 1] + ways[i - 2])
        
        return ways[n - 1]

# @lc code=end


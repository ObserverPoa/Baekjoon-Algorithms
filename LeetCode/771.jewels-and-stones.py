#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_dict = {}
        for jewel in jewels:
            jewels_dict[jewel] = True
        
        count = 0
        for stone in stones:
            if stone in jewels_dict:
                count += 1
        return count

        # 한줄 풀이
        # return sum(s in jewels for s in stones)
# @lc code=end


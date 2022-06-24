#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        import collections
        
        solutions = []

        # 양수와 음수, 0 각각의 개수 카운팅
        positives = collections.Counter([num for num in nums if num > 0])
        negatives = collections.Counter([num for num in nums if num < 0])
        zero_count = nums.count(0)
        
        # + - -
        for pnum, count in positives.items():
            if pnum >= 2:
                for nnum, count in negatives.items():
                    if -1 * nnum < pnum / 2:
                        test = (pnum + nnum) * -1
                        if test in negatives:
                            solutions.append([pnum, nnum, (pnum + nnum) * -1])
                    elif -1 * nnum == pnum / 2 and count >= 2:
                        solutions.append([pnum, nnum, nnum])
    
        # - + +
        for nnum, count in negatives.items():
            if nnum <= -2:
                for pnum, count in positives.items():
                    if pnum < -1 * nnum / 2:
                        test = (pnum + nnum) * -1
                        if test in positives:
                            solutions.append([nnum, pnum, (pnum + nnum) * -1])
                    elif pnum == -1 * nnum / 2 and count >= 2:
                        solutions.append([nnum, pnum, pnum])
        
        if zero_count >= 1:
            # 0 0 0
            if zero_count >= 3:
                solutions.append([0, 0, 0])
            
            # + - 0
            for pnum in positives.keys():
                if pnum * -1 in negatives:
                    solutions.append([pnum, pnum * -1, 0])

        return solutions
# @lc code=end


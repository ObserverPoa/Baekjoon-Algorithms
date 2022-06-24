#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        merged = [intervals.pop(0)]
        for start, end in intervals:
            prev_start, prev_end = merged[-1]
            if start <= prev_end: # 겹치는 경우
                merged[-1] = [prev_start, max(prev_end, end)]
            else: # 겹치치 않는 경우
                merged.append([start, end])
            
        return merged

        
# @lc code=end


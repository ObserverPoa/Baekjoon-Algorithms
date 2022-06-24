#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer, past = [0] * len(temperatures), []

        for i in range(len(temperatures)):
            while past and temperatures[past[-1]] < temperatures[i]:
                answer[past[-1]] = i - past[-1]
                past.pop()
            
            past.append(i)

        return answer

        
# @lc code=end


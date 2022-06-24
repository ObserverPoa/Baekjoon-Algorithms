#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    dial = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        elif len(digits) == 1:
            return list(self.dial[int(digits[0]) - 2])
        else:
            combinations = []
            suffix = self.letterCombinations(digits[1:])
            for char in self.dial[int(digits[0]) - 2]:
                combinations += [char + s for s in suffix]
            return combinations

# @lc code=end


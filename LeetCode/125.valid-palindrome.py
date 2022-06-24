#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert uppercase to lowercase and
        # remove all non-alphanumeric characters
        alphanumeric = []
        for c in s:
            if c.isalnum():
                alphanumeric.append(c.lower())
        

        # compare forward and backward
        for i in range(len(alphanumeric) // 2):
            if (alphanumeric[i] != alphanumeric[-1 * i - 1]):
                return False
        return True
            

# @lc code=end


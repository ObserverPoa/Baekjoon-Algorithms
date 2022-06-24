#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # for size in range(len(s), 0, -1):
        #     for i in range(len(s) - size + 1):
        #         substr = s[i : i + size]
        #         if substr == substr[::-1]:
        #             return substr

        if len(s) <= 1:
            return s

        def get_palindrome(mid: float) -> str:
            if mid.is_integer(): # 홀수 길이 palindrome
                left = int(mid - 1)
                right = int(mid + 1)
            else: # 짝수 길이 palindrome
                left = int(mid - 0.5)
                right = int(mid + 0.5)
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1 : right]

        max_palindrome = s[0]
        mid = (len(s) - 1) / 2
        max_palindrome = max(max_palindrome,
                            get_palindrome(mid),
                            key=len)

        for i in range(1, len(s)):
            #이미 최대 길이의 palindrome을 찾았을 때
            if len(max_palindrome) >= len(s) - i:
                break
            
            max_palindrome = max(max_palindrome,
                                get_palindrome(mid - i / 2),
                                get_palindrome(mid + i / 2),
                                key=len)

            

        return max_palindrome


        
# @lc code=end


#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        used = {}
        front = 0 # 서브스트링의 시작인덱스
        for i in range(len(s)):
            if s[i] in used and used[s[i]] >= front: # 현재 서브스트링의 문자와 중복되는 경우
                front = used[s[i]] + 1 # 서브스트링의 시작인덱스 갱신
            else:
                maxlen = max(maxlen, i - front + 1) # 계속 최대 서브스트링 길이 갱신
            used[s[i]] = i # 사용된 문자의 인덱스 갱신

        return maxlen

# @lc code=end


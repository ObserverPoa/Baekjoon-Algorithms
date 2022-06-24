#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0

        counter = collections.Counter()

        for right, char in enumerate(s, 1):
            counter[char] += 1

            # 현재 window가 같은 char로 구성되기 위한 최소 replace 횟수
            min_replace = right - left - counter.most_common(1)[0][1]

            if min_replace > k:
                counter[s[left]] -= 1
                left += 1

        # for문에서 window의 크기는 유지되거나 증가된다. 절대 감소하지 않는다.
        return right - left




# @lc code=end


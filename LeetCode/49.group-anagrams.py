#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = collections.defaultdict(list)
        for word in strs:
            groups[''.join(sorted(word))].append(word)
        return list(groups.values())
        
# @lc code=end


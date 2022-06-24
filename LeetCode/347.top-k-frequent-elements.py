#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import collections
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [item[0] for item in collections.Counter(nums).most_common(k)]
# @lc code=end


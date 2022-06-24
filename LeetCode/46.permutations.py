#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(prefixes: list[int], path: list[int]):
            if len(path) == len(nums):
                result.append(path)
                return
            for i in range(len(prefixes)):
                dfs(prefixes[:i] + prefixes[i + 1:], path + [prefixes[i]])

        result = []
        dfs(nums, [])
        return result

        # itertools 사용 (*permutation: 순열)
        # return list(itertools.permutations(nums))
# @lc code=end


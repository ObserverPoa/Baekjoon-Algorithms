#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(start: int, path: list[int]):
            subsets.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
        
        subsets = []
        dfs(0, [])
        return subsets


# @lc code=end


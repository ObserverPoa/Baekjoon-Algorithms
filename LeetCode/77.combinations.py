#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def dfs(start: int, k: int, path: list[int]):
            if k == 0:
                combinations.append(path[:])
            else:
                for i in range(start, n + 1 - (k - 1)): # k를 0까지 감소시킬 수 있는 i만 path 에 append 한다.
                    path.append(i)
                    dfs(i + 1, k - 1, path)
                    path.pop()
            return

        combinations = []
        dfs(1, k, [])
        return combinations
# @lc code=end


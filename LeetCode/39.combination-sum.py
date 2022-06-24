#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(start: int, sum: int, combination = list[int]):
            if sum == target:
                combinations.append(combination[:])
            else:
                for i in range(start, len(candidates)):
                    if sum + candidates[i] > target: # 타겟보다 합이 크게 되는 candidate가 나오면 loop을 탈출한다. (미리 정렬해두었기 때문에 문제 없음.)
                        break
                    combination.append(candidates[i])
                    dfs(i, sum + candidates[i], combination)
                    combination.pop()
            return

        combinations = []
        candidates.sort()
        dfs(0, 0, [])
        return combinations
# @lc code=end


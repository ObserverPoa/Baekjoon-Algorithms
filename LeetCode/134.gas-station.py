#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # 경로가 존재하지 않는 경우
        if sum(gas) < sum(cost):
            return -1

        # 그 외의 경우, 경로가 무조건 존재한다.
        # 시작점이 될 수 없는 경우, 시작점을 한칸 뒤로 미룬다.
        start, fuel = 0, 0
        for i in range(len(gas)):
            if fuel + gas[i] - cost[i] >= 0:
                fuel += gas[i] - cost[i]
            else:
                start = i + 1
                fuel = 0

        return start

# @lc code=end


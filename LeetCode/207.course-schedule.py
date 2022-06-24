#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 그래프에 순환구조가 있는지 확인하는 문제이다.

        # 그래프 생성
        graph = collections.defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])

        visited = set() # 한번 방문한 노드를 다시 방문하지 않기 위함
        prevs = set() # dfs탐색 시 지나온 노드를 확인하는데 사용.

        def dfs(num: int):
            visited.add(num)
            prevs.add(num)

            for near in graph[num]:
                if near in prevs: # 순환구조 발견
                    return False
                if near not in visited and not dfs(near): # 방문하지 않았던 노드만 방문하며, dfs의 반환값이 false일 경우 상위 호출레벨로 false를 즉시 반환.
                    return False
                    
            prevs.remove(num)
            return True

        for i in range(numCourses): # 모든 노드에 대해 dfs수행 (단, 이전 dfs수행시 이미 방문했던 노드들은 제외).
            if i not in visited and not dfs(i):
                return False

        return True
# @lc code=end


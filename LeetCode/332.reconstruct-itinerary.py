#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
import collections
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # 그래프 구조 생성 (각 노드의 인접 노드 목록이 알파벳순으로 정렬되도록)
        # dfs를 하는데, 각 노드에 인접한 모든 노드를 알파벳 순으로 방문 (모든 간선을 지나가도록 한다.)
        # 사전 순서의 오일러 경로를 찾는 문제.

        def dfs(airport: str):
            while graph[airport]:
                dfs(graph[airport].pop()) # 인접 공항으로 이동하면서 인접 공항으로 가는 간선을 삭제한다
            itinerary.append(airport) # 더 이상 이동할 수 없는 공항을 일정의 뒷부분에 오도록 하기 위해, while문을 마친 후 itinerary에 넣는다.
        
        graph = collections.defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        for nears in graph.values():
            nears.sort(reverse=True)
        
        itinerary = []
        dfs("JFK")
        return itinerary[::-1]
        


# @lc code=end


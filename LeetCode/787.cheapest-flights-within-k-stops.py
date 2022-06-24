#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
import collections, heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, p in flights:
            graph[u].append((v, p))

        Q = [(0, -1, src)]
        min_stops = [k] * n

        while Q:
            price, stops, node = heapq.heappop(Q)

            if node == dst:
                return price

            # heap에서 각 노드에 대해 처음 나오는 경로는 그 노드로의 최소 경로이지만, 
            # dst까지 경로를 계속 진행했을 때 stops가 k를 초과할 수 있으므로,
            # 동일 노드에 대해 price가 더 높은 경로(heap에서 이 node에 대해 최초 이후로 나오는 경로)라도 stops가 더 낮으면 탐색을 진행한다.
            # 단순히 stops가 k미만인 모든 경로를 다 탐색하게 하면(min_stops 미사용), 시간복잡도가 증가한다.
            if stops < min_stops[node]: 
                min_stops[node] = stops

                for v, p in graph[node]:
                    heapq.heappush(Q, (price + p, stops + 1, v))

        return -1

# @lc code=end


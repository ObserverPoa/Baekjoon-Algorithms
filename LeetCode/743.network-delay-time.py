#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
import collections
import heapq
import sys
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # 그래프 생성
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # 다익스트라 알고리즘으로 최적 경로 구하기
        dist = collections.defaultdict(int) # k에사 각 노드까지의 최적딜레이
        Q = [(0, k)] # 최적 노드를 우선적으로 그래프를 bfs 탐색하기 위한 priority queue

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist: # 노드를 최초로 dist에 넣을 때가 그 노드로의 가장 최소 소요시간 값을 갖고 있다.
                dist[node] = time
                for v, w in graph[node]:
                    heapq.heappush(Q, (time + w, v))

        # 모든 최적 경로들의 소요시간 중 최대값 반환.
        if len(dist) == n:
            return max(dist.values())

        # k노드가 모든 노드와 연결되어있지 않은 경우 -1 반환
        return -1

# @lc code=end


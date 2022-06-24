#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        # 최초 리프노드들
        leaves = [
            v for v in graph if len(graph[v]) == 1
        ]
        
        # 리프노드를 계속해서 삭제해가며, 최종적으로 그래프에 2개 이하의 노드만 남았을때
        # 그래프의 중앙에 위치한 2개 이하의 노드가 MHT의 root이다.
        # 여기에서, 그래프의 중앙에 위치해 있다는 말은 그래프 내의 가장 긴 path의 중앙에 위치해 있다는 것을 뜻한다.
        # 드러나는 리프노드들을 계속 일괄삭제하면 그래프의 중앙에 위치한 노드만 남을 수 밖에 없다.
        # 왜냐면 그래프 중앙에 위치한 노드는 다른 모든 노드까지의 거리의 최대값을 가장 작게 하는 노드이기 때문이다.
        while n > 2:
            n -= len(leaves)

            # 현재 리프노드들과 인접한 노드들만이 현재 리프노드들을 모두 삭제한 뒤의 그래프의 리프노드 후보가 될 수 있다.
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves
            
        return leaves


# @lc code=end


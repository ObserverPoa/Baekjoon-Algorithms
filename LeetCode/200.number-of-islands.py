#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def DFS(x, y):
            grid[x][y] = "0"
            for i, j in zip(dx, dy):
                if x + i >= 0 and x + i < len(grid) \
                        and y + j >= 0 and y + j < len(grid[x]) \
                        and grid[x + i][y + j] == "1":
                    DFS(x + i, y + j)

        islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    DFS(x, y)
                    islands += 1
        
        return islands
            
# @lc code=end


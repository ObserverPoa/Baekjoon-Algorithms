#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # 우측 상단 모서리부터 탐색을 시작해서 행 또는 열을 하나씩 배제하면서 왼쪽 아래 모서리까지 탐색을 진행한다.
        # 왼쪽 하단 모서리로부터 탐색을 시작해서 반대 방향으로 탐색을 해도 된다.
        # 시간복잡도는 O(m + n) 이다.

        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
            else:
                return True

        return False
# @lc code=end


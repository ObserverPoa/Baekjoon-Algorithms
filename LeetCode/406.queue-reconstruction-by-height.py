#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        queue = []
        for person in sorted(people, key=lambda x: (-x[0], x[1])):
            queue.insert(person[1], person)
        return queue
# @lc code=end


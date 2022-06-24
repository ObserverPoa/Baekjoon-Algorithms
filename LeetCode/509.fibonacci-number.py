#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    dic = {}
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        elif n in self.dic:
            return self.dic[n]
        else:
            self.dic[n] = self.fib(n - 1) + self.fib(n - 2)
            return self.dic[n]
# @lc code=end


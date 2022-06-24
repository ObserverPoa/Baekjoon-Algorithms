#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        import sys

        max_profit = 0
        best_buy_price = sys.maxsize
        for price in prices:
            max_profit = max(max_profit, price - best_buy_price)
            best_buy_price = min(best_buy_price, price)


        return max_profit
        
# @lc code=end


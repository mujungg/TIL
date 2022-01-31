import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            profit = max(prices[i + 1:]) - prices[i]
            if profit > max_profit:
                max_profit = profit
        return max_profit

    # 타임리밋..

    def solution_02(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))

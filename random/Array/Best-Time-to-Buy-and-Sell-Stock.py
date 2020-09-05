from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 max_profit = max(max_profit, prices[j] - prices[i])
        
#         return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit


sol = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(sol.maxProfit(prices))

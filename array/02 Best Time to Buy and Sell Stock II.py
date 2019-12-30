# Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        if length <= 1:
            return 0
        
        profit = 0
        j = 0
        
        for i in range(1, length):
            if prices[i-1] > prices[i]:
                profit +=   prices[i-1] - prices[j]
                j = i
        if prices[length-1] > prices[j]:
            profit +=   prices[length-1] - prices[j]
        
        return profit


prices = [1,2,3,4,5]

solution = Solution()
print(solution.maxProfit(prices))
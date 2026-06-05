class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                continue
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]
        return profit
            

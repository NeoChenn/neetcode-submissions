class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy at lowest seen so far, and sell at each possible opportunity
        #update if profit > max profit.
        #So for pointer l and r starting at 0, move r one by one. If r cheaper
        #than l, update l. Otherwise, attempt to update max profit.
        #this works because can only sell at a time later than buy
        #and already attempted all possible profits at the lowest buy so far
        #so updating l when a lower buy is found is optimal.
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue
            profit = max(profit, prices[r]-prices[l])
            r += 1
        return profit
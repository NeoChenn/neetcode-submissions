class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        keep track of buying day, which will be updated to the cheapest day we've seen so far
        compare current profit with profit if it were to be sold on the current day
        """

        profit, buyDay = 0, 0
        for day in range(len(prices)):
            if prices[day] < prices[buyDay]:
                buyDay = day
            profit = max(profit, prices[day] - prices[buyDay])

        return profit
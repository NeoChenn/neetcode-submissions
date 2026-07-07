class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}
        
        def recursion(i, acc, length):
            if (i, acc, length) in memo:
                return memo[(i, acc, length)]
            if acc == amount:
                return length
            if acc > amount or i >= len(coins):
                return 2**31 - 1

            memo[(i, acc, length)] = min(recursion(i, acc + coins[i], length + 1), recursion(i + 1, acc, length))
            return memo[(i, acc, length)]
        
        res = recursion(0, 0, 0) 
        if res == 2**31 - 1:
            return -1
        return res
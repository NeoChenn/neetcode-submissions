class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def recursion(i):
            if i in memo:
                return memo[i]
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0

            num1 = recursion(i + 1)
            if i + 1 >= len(s) or int(s[i:i + 2]) > 26:
                num2 = 0
            else:
                num2 = recursion(i + 2)
            
            memo[i] = num1 + num2
            return memo[i]

        return recursion(0)
            

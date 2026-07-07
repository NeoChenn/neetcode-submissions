class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def recursion(index):
            if index == len(s):
                return True
            if index in memo:
                return memo[index]
            
            for i in range(index, len(s)):
                if s[index:i+1] in wordDict and recursion(i + 1):
                    memo[index] = True
                    return True
            
            memo[index] = False
            return False

        return recursion(0)

            
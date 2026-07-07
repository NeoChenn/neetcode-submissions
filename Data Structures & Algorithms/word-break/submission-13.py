class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)  # O(1) lookup instead of O(n)
        
        def recursion(index):
            if index in memo:
                return memo[index]
            if index == len(s):
                return True

            for i in range(index, len(s)):
                if s[index:i + 1] in wordSet and recursion(i + 1):
                    memo[index] = True
                    return True
            
            memo[index] = False
            return False

        return recursion(0)
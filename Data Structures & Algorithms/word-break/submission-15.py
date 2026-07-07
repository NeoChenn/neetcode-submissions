class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        wordSet = set(wordDict)
        
        def recursion(index, string):
            if (index, string) in memo:
                return memo[(index, string)]
            if string and string not in wordSet:
                return False
            if index == len(s): 
                return True

            for i in range(index, len(s)):
                word = s[index:i + 1]
                memo[(i + 1, word)] = recursion(i + 1, word) 
                if memo[(i + 1, word)]:
                    return True
            return False

        return recursion(0, "")

            
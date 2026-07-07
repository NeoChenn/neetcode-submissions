class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def recursion(index, string):
            if (index, string) in memo:
                return memo[(index, string)]
            if string and string not in wordDict:
                return False
            if index == len(s): 
                return True

            for i in range(index, len(s)):
                memo[(i + 1, s[index:i + 1])] = recursion(i + 1, s[index:i + 1]) 
                if memo[(i + 1, s[index:i + 1])]:
                    return True
            return False

        return recursion(0, "")

            
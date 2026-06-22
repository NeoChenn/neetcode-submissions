class Solution:
    def partition(self, string: str) -> List[List[str]]:
        def checkPalindrome(s):
            i, j = 0, len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        res = []
        attempt = []
        def backtrack(remaining):
            if not remaining:
                for substring in attempt:
                    if not checkPalindrome(substring):
                        return
                res.append(attempt.copy())
                return
        
            for i in range(len(remaining)):
                substr = remaining[:(i + 1)]
                if not checkPalindrome(substr):   
                    continue
                attempt.append(substr)
                backtrack(remaining[i + 1: len(remaining)])
                attempt.pop()

        backtrack(string)
        return res

            
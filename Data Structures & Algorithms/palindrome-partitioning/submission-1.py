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
            slen = len("".join(attempt.copy()))
            if slen >= len(string):
                for substring in attempt:
                    if not checkPalindrome(substring):
                        return
                res.append(attempt.copy())
                return
        
            for i in range(len(remaining)):
                attempt.append(remaining[:(i + 1)])
                backtrack(remaining[i + 1: len(remaining)])
                attempt.pop()

        backtrack(string)
        return res

            
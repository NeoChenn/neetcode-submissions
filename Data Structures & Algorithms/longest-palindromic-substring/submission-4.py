class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        #odds
        for i in range(len(s)):
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            attempt = s[l + 1:r]
            if len(res) < len(attempt):
                res = attempt

        #events
        for i in range(1, len(s)):
            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            attempt = s[l + 1:r]
            if len(res) < len(attempt):
                res = attempt   
        
        return res
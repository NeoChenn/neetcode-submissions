class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        maxPalin = ""

        def oddPalinLength(i, s):
            length = 1
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 2
                r += 1
                l -= 1
            return [length, s[l + 1: r]]


        def evenPalinLength(i, j, s):
            length = 0
            l, r = j, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 2
                r += 1
                l -= 1
            return [length, s[l + 1: r]]

        for i in range(len(s)):
            length, string = oddPalinLength(i, s)
            if length > maxLength:
                maxLength = length
                maxPalin = string

        for i in range(1, len(s)):
            length, string = evenPalinLength(i, i - 1, s)
            if length > maxLength:
                maxLength = length
                maxPalin = string

        return maxPalin
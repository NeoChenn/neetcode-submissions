class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalin(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                # try skipping either side, check if remainder is palindrome
                return isPalin(s, i+1, j) or isPalin(s, i, j-1)
            i += 1
            j -= 1
        return True
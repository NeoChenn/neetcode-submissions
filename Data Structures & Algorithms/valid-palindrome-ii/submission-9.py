class Solution:
    def validPalindrome(self, s: str) -> bool:

        def pal(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        l, r = 0, len(s) - 1
        skipped = False
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] != s[r] and not skipped:
                if s[l + 1] == s[r] and s[l] == s[r - 1]:
                    return pal(l + 1, r) or pal(l, r - 1)
                elif s[l + 1] == s[r]:
                    skipped = True
                    l += 2
                    r -= 1
                elif s[l] == s[r - 1]:
                    skipped = True
                    l += 1
                    r -= 2
                else:
                    return False
            else:
                return False

        return True
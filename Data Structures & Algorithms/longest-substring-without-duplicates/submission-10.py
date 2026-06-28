class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        longest = 0
        if len(s) == 0:
            return 0

        i, j = 0, 0
        while j < len(s):
            while s[j] in window:
                window.remove(s[i])
                i += 1
            window.add(s[j])
            longest = max(longest, len(window))
            j += 1

        return longest
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        longest = 1
        if len(s) == 0:
            return 0

        i, j = 0, 0
        window.add(s[j])
        while j < len(s) - 1:
            j += 1
            while s[j] in window:
                window.remove(s[i])
                i += 1
            window.add(s[j])
            longest = max(longest, len(window))

        return longest
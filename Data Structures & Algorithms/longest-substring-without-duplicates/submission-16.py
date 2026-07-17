class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        longest = 1
        l = 0
        if len(s) == 0:
            return 0
        window.add(s[0])
        for r in range(1, len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            longest = max(longest, len(window))

        return longest
        # zxyyzx
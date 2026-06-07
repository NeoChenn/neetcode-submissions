class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0
        length = 0
        for r in range(len(s)):
            if s[r] in mySet:
                while s[l] != s[r]:
                    mySet.remove(s[l])
                    l += 1
                mySet.remove(s[l])
                l += 1
            mySet.add(s[r])
            length = max(length, r - l + 1)
        return length
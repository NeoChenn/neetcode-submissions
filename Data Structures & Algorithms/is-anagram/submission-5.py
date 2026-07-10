class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tMap = {}
        sMap = {}

        for c in t:
            if c not in tMap:
                tMap[c] = 0
            tMap[c] += 1

        for c in s:
            if c not in sMap:
                sMap[c] = 0
            sMap[c] += 1

        return tMap == sMap
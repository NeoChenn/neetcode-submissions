class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = {}
        if len(s2) < len(s1):
            return False
            
        for c in s1:
            if c not in s1map:
                s1map[c] = 0
            s1map[c] += 1

        l, r = 0, len(s1) - 1
        windowMap = {}
        for i in range(len(s1)):
            if s2[i] not in windowMap:
                windowMap[s2[i]] = 0
            windowMap[s2[i]] += 1 

        while r < len(s2) - 1:
            if s1map == windowMap:
                return True
            windowMap[s2[l]] -= 1
            if windowMap[s2[l]] == 0:
                windowMap.pop(s2[l])
            l += 1
            r += 1
            if s2[r] not in windowMap:
                windowMap[s2[r]] = 0
            windowMap[s2[r]] += 1

        return s1map == windowMap 
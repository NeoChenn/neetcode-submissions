class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        windowMap = {}
        for c in s1:
            if c in s1Map:
                s1Map[c] +=1
            else:
                s1Map[c] = 1
        
        l = 0
        r = 0
        while r < len(s2):
            if s2[r] in windowMap:
                windowMap[s2[r]] += 1
            else:
                windowMap[s2[r]] = 1

            while r - l + 1 > len(s1):
                windowMap[s2[l]] -= 1
                if windowMap[s2[l]] == 0:
                    windowMap.pop(s2[l])
                l += 1

            if s1Map == windowMap:
                return True
            
            r += 1

        return False

        #permutation. Order matters.
        #Sliding window
        #Start both pointers l and r at index 0
        #max window size = len(s1)
        #keep track of frequency of characters
        #if s1map == s2map then return true
        #if r reaches end of s2  
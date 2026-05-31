class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for a in s:
            if a in smap:
                smap[a] +=1
                continue
            smap[a] = 0
        
        for a in t:
            if a in tmap:
                tmap[a] += 1
                continue
            tmap[a] = 0
        
        if smap == tmap:
            return True
        return False
        
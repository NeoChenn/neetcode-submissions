class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #hashmap would have O(26) space
        #sorting would have O(nlogn + nlogm) time
        
        sMap = {}
        tMap = {}
        def fillMap(string, hashmap):
            for c in string:
                if c not in hashmap:
                    hashmap[c] = 0
                hashmap[c] += 1
        
        fillMap(s, sMap)
        fillMap(t, tMap)
        if sMap == tMap:
           return True 
        return False
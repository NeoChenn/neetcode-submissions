class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for c in magazine:
            if c not in hashmap:
                hashmap[c] = 0
            hashmap[c] += 1

        for c in ransomNote:
            if c not in hashmap or hashmap[c] == 0:
                return False
            hashmap[c] -= 1
        
        return True
        
        #a : 1
        #b : 1
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        for c in s:
            if c not in hashmap:
                hashmap[c] = 0
            hashmap[c] += 1

        #accumulate evens.
        #if odd, add it completely once. Then, add it minus 1
        count = 0
        odd = False
        for freq in list(hashmap.values()):
            if freq % 2 == 0:
                count += freq
            else:
                if not odd:
                    odd = True
                    count += freq
                else:
                    count += (freq - 1)
        return count
class Solution:
    def countSubstrings(self, s: str) -> int:
        #for each char, have a l and r pointer at same index. 
        #if l and r are the same, increment count and "widen" the window
        #repeat until l and r are not the same OR l or r are out of bounds
        #this gets us all odd palindromes

        #repeat process with contiguous pairs of chars to get all even palindromes
        #racecar

        count = 0

        #odd pals
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        #even pals
        for i in range(len(s) - 1):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count
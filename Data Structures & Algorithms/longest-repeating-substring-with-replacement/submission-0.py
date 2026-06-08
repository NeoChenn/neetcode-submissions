class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def occurencesOfMostFrequentChar(count):
            highest = 0
            for key in count:
                highest = max(highest, count[key])
            return highest
        
        count = {}
        res = 0

        l, r = 0, 0
        while r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            
            while (r - l + 1) - occurencesOfMostFrequentChar(count) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res

        #Sliding window approach:
        #Count occurrences of each letter in window
        #while r < len(s)
        #If len(window)-(occurrences of most frequent character) > k
            #increment l until len(window)-(character with most occurrences) <= k 
        #else update res to len(window) and increment r
    

        #Start with l and r from 0. Count characters with hashmap. 
        #to find highest value. Iterate through all keys.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        sliding window:
        hashmap = {letter: freq}
        for r in range(1, len(s)):
            l += 1 while sum(all freqs) - largest freq > k
        """
        maxLength = 1
        hashmap = {s[0] : 1}
        mFreq = 1
        l = 0
        for r in range(1, len(s)):
            if s[r] not in hashmap:
                hashmap[s[r]] = 0
            hashmap[s[r]] += 1
            mFreq = max(mFreq, hashmap[s[r]])

            freqs = hashmap.values()
            while (r - l + 1) - mFreq > k:
                hashmap[s[l]] -= 1
                if hashmap[s[l]] == 0:
                    hashmap.pop(s[l])
                l += 1
            maxLength = max(maxLength, r - l + 1)
        return maxLength
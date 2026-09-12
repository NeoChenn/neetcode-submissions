class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charToFreq = {}
        for c in s:
            if c not in charToFreq:
                charToFreq[c] = 0
            charToFreq[c] += 1
        
        res = []
        for c in order:
            if c in charToFreq:
                for _ in range(charToFreq[c]):
                    res.append(c)
                charToFreq.pop(c)
        
        for c, freq in list(charToFreq.items()):
            for _ in range(freq):
                res.append(c)
        
        return "".join(res)

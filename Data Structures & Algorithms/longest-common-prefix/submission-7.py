class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        minLen = 200
        for s in strs:
            minLen = min(len(s), minLen)

        for i in range(minLen):
            mismatch = False
            cur = strs[0][i]
            for s in strs:
                if cur != s[i]:
                    mismatch = True
                    break
            if mismatch:
                break
            res = res + cur
        
        return res
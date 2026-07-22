class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or "" in strs:
            return ""
        res = []
        currIdx = 0
        endReached = False
        while not endReached:
            res.append(strs[0][currIdx])
            for s in strs:
                if s[currIdx] != res[-1]:
                    res.pop()
                    return "".join(res)
                if len(res) == len(s):
                    endReached = True
            currIdx += 1
        return "".join(res)

            
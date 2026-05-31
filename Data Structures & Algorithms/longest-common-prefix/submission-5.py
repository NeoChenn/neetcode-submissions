class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        strs.sort()
        for char in strs[0]:
            if (i >= len(strs[0])):
                return prefix
            for str in strs:
                if char!=str[i]:
                    return prefix
            prefix += char
            i+=1
        return prefix

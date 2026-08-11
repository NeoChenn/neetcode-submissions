class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = 0
        output = []
        for i in range(min(len(word1), len(word2))):
            output.append(word1[p])
            output.append(word2[p])
            p += 1
        output = "".join(output)
        if len(word2) > len(word1):
            output += word2[p:len(word2)]
        elif len(word1) > len(word2):
            output += word1[p:len(word1)]

        return output
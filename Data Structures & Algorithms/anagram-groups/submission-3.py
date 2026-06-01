class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for str in strs:
            count = [0 for i in range(26)]
            for c in str:
                count[ord(c)-ord('a')] += 1
            key = tuple(count)
            if key not in map:
                map[key] = []
            map[key].append(str)
        return list(map.values())

#count a-z as key for map. If same key, a
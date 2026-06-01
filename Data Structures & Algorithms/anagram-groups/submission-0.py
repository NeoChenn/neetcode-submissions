class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key not in map:
                map[key] = []
            map[key].append(str)
            finalList = list(map.values())
        return finalList
 

#for each str in strs, map stores sorted str as key, empty array as value if key 
#key does not exist. If it does, push original str into value
#return all values of hashmap

#To check for two strings, set up a hash map for each and compare hash maps.
#Group words with the same hash map.
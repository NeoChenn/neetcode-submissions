class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = {}
        res = []
        for n in nums:
            if n not in map:
                map[n] = 1
            map[n] += 1

        ls = sorted(list(map.keys()), key = lambda x : map[x], reverse=True)
        for i in range(k):
            res.append(ls[i])

        return res

        # [1,2,2,3,3,3,3]
        # 1 -> 1
        # 2 -> 2
        # 3 -> 4

        #[]

        
    
        
    #hashmap for frequency count
    #sort keys in descending order based on frequency count
    #update the k array in real time?

    #sort,


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap where num is the key, freq is the value

        #sort hashmap.items by freq and return the k most frequent keys (nlogn + n)
        #OR
        #heap hashmap.items and pop k times. (n + klogn)
        hashmap = {}
        res = []
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 0
            hashmap[n] += 1

        heap = [(v, k) for k, v in list(hashmap.items())]
        heapq.heapify_max(heap)
        for i in range(k):
            res.append(heapq.heappop_max(heap)[1])

        return res
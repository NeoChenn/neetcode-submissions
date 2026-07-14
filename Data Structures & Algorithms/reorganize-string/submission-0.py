class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        hashmap where letter is key, frequency is value
        maxheap to find most frequent
        pick most frequent. If creates adj, pick snd most frequent and so on. 
        if no picks, return ""
        if freq == 0, delete from hashmap
        """
        
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1

        maxHeap = [(f, k) for k, f in list(freq.items())]
        heapq.heapify_max(maxHeap)

        res = []
        while freq:
            mostFreq = heapq.heappop(maxHeap)
            while res and res[-1] == mostFreq[1]:
                if not maxHeap:
                    return ""
                mostFreq = heapq.heappop(maxHeap)
            res.append(mostFreq[1])
            freq[mostFreq[1]] -= 1
            if freq[mostFreq[1]] == 0:
                freq.pop(mostFreq[1])
            maxHeap = [(f, k) for k, f in list(freq.items())]
            heapq.heapify_max(maxHeap)

        return "".join(res)
            
            


        
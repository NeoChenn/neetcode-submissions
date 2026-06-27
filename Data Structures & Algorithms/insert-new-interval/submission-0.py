class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #intervals is an array of non-overlapping intervals, sorted in ascending order by start
        
        res = []
        for i, (start, end) in enumerate(intervals):
            if newInterval[0] > end:
                res.append([start, end])
            elif newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        
        res.append(newInterval)
        return res
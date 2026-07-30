"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        hashmap = {}
        res = 0
        curRooms = 0
        for interval in intervals:
            if interval.start not in hashmap:
                hashmap[interval.start] = 0
            if interval.end not in hashmap:
                hashmap[interval.end] = 0
            hashmap[interval.start] += 1
            hashmap[interval.end] -= 1

        timeline = sorted(list(hashmap.items()))
        for time, rooms in timeline:
            curRooms += rooms
            res = max(res, curRooms)

        return res
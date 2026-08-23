"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        rooms = 0
        rooms += 1 when meeting starts, rooms -= 1 when meeting ends
        {0 : 1, 5 : 1, 10 : -1, 15 : 1, 20 : -1, 40 : -1}
        """

        timeline = {}
        rooms = 0
        res = 0
        for interval in intervals:
            if interval.start not in timeline:
               timeline[interval.start] = 0 
            timeline[interval.start] += 1
            if interval.end not in timeline:
               timeline[interval.end] = 0 
            timeline[interval.end] -= 1
        for time, room in sorted(list(timeline.items())):
            rooms += room
            res = max(res, rooms)
        return res
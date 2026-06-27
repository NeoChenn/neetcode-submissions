"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        freeFrom = 0
        for interval in intervals:
            if interval.start < freeFrom:
                return False
            freeFrom = interval.end
        return True
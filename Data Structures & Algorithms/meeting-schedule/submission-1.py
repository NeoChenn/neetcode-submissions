"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def start(m):
        return m.start

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)

        i, j = 0, 1
        while j < len(intervals):
            if intervals[i].end > intervals[j].start:
                return False
            i += 1
            j += 1
        return True
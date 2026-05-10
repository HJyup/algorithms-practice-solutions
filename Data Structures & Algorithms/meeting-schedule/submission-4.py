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

        last_meeting_end = -1

        for interval in intervals:
            if last_meeting_end <= interval.start:
                last_meeting_end = interval.end
            else:
                return False

        return True

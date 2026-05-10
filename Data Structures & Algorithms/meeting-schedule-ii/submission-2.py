"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # We need to minimise search for the room which end first
        # Since we keep track of global min we can use heap to get a possbility for O(1) lookup 
        # To insert/remove we will do it in O(log(n))
        # since if first global min is end later than start of this current interval there is no way
        # to allocate to existing room since all of them end later
        # this solution will give us O(n * log(n))
        # time complexity is O(n) since we can have all rooms in heep in the worst case
        intervals.sort(key = lambda x : x.start)
        rooms = []

        for interval in intervals:
            if rooms and interval.start >= rooms[0]:
                heapq.heappushpop(rooms, interval.end)
            else:
                heapq.heappush(rooms, interval.end)

        number_of_rooms = len(rooms)
        return number_of_rooms
        
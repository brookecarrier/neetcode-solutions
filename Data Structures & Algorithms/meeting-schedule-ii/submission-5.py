"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # find max overlaps
        # sort start and end times
        # every time new meeting starts, currmeetings++
        # if end time is less than start time, curr meetings--
        # keep track of max curr meetings

        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()

        currMeetings = 0
        maxMeetings = 0
        e = 0

        for start in starts:
            currMeetings += 1

            if ends[e] <= start:
                currMeetings -= 1
                e += 1
            
            maxMeetings = max(maxMeetings, currMeetings)
        
        return maxMeetings

        
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x: x.start)
        n = len(intervals)
        for i in range(n-1):            
            if intervals[i].end > intervals[i+1].start:
                return False
        return True


def canAttendMeetings(self, intervals):
    intervals.sort(key=lambda x: x.start)

    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i-1].end:
            return False

    return True
  
  class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """      
        intervals.sort(key=lambda x:x[0])
        n = len(intervals)
        for i in range(n-1):
            if intervals[i][-1] > intervals[i+1][0]:
                return False
        return True
            

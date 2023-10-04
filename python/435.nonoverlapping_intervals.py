"""
greedy
"""
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        end, cnt = -sys.maxint, 0
        for s, e in sorted(intervals, key=lambda x:x[1]):
            if s >= end:
                end = e
            else:
                cnt += 1
        return cnt
    
# https://www.youtube.com/watch?v=nONCGxWoUfM
# O(nlogn)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res
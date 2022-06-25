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
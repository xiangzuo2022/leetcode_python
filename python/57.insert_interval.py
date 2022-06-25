# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
    	intervals.append(newInterval)
    	intervals.sort(key=lambda x:x.start)
    	length = len(intervals)
    	res = []
    	for i in range(length):
    		if res==[]:
    			res.append(intervals[i])
    		else:
    			size = len(res)
    			if res[size-1].start <= intervals[i].start <= res[size-1].end:
    				res[size-1].end = max(intervals[i].end, res[size-1].end)
    			else:
    				res.append(intervals[i])
    	return res



# ****** The Second Time ********
# 解题思路：最简单的方法是将要插入的区间和原来的区间合在一起排序，然后按照merge intervals的方法来编程。
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x.start)
        res = []
        for i in range(len(intervals)):
            if res == []:
                res.append(intervals[i])
            else:
                size = len(res)
                
                if res[size-1].start <= intervals[i].start <= res[size-1].end:
                    res[size-1].end = max(res[size-1].end, intervals[i].end)
                else:
                    res.append(intervals[i])
        return res
























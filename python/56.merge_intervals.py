# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
    	intervals.sort(key=lambda x:x.start)
    	length = len(intervals)
    	res = []
    	for i in range(length):
    		if res == []:
    			res.append(intervals[i])
    		else:
    			size = len(res)
    			if res[size-1].start <= intervals[i].start<= res[size-1].end:
    				res[size-1].end = max(intervals[i].end, res[size-1].end)
    			else:
    				res.append(intervals[i])
    	return res


#  ****** The Second Time ********
# 解题思路：先将区间按照每个start的值来排序，排好序以后判断一个区间的start值是否处在前一个区间中，
# 如果在前一个区间中，那么合并；如果不在，就将新区间添加。
# 一开始忘记要排序了；网上做法是朝前看,貌似我的往后看不work

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        intervals.sort(key=lambda x:x.start)
        n = len(intervals)
        res = []
        for i in range(n):
            if res == []:
                res.append(intervals[i])
            else:
                size = len(res)
                if res[size-1].start <= intervals[i].start<= res[size-1].end:
                    res[size-1].end = max(intervals[i].end, res[size-1].end)
                else:
                    res.append(intervals[i])
        return res
      
# official solution
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        merged= []
        for list in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < list[0]:
                merged.append(list)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], list[1])
        return merged
      
      
"""
Greedy: another implementation 
"""
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n == 0: return 0
        result = []
        intervals.sort(key=lambda x:x[0])
        result.append(intervals[0])
        for i in range(1, n):
            last = result[-1]
            if last[1] >= intervals[i][0]:
                result[-1] = [last[0], max(last[1], intervals[i][1])]
            else:
                result.append(intervals[i])
        return result
    
# https://www.youtube.com/watch?v=44H3cEC2fFM
# deal with all cases
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]] # add the first one in the res can avoid many edge cases

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                # [1, 5], [2, 4] = [1, 5]
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])
        return res








            























# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        numRoom = available = 0
        i = 0
        for start in starts:
            while ends[i] <= start:
                available += 1
                i += 1
            if available:
                available -= 1
            else:
                numRoom += 1
        return numRoom


"""
use min heap O(nlogn)
一种使用最小堆来解题的方法，这种方法先把所有的时间区间按照起始时间排序，然后新建一个最小堆，开始遍历时间区间，如果堆不为空，
且首元素小于等于当前区间的起始时间，我们去掉堆中的首元素，把当前区间的结束时间压入堆，由于最小堆是小的在前面，那么假如首元素
小于等于起始时间，说明上一个会议已经结束，可以用该会议室开始下一个会议了，所以不用分配新的会议室，遍历完成后堆中元素的个数即
为需要的会议室的个数.
"""
import heapq
def minMeetingRooms(self, intervals):
    intervals.sort(key=lambda x: x.start)
    heap = []  # stores the end time of intervals
    for i in intervals:
        if heap and i.start >= heap[0]:
            # means two intervals can use the same room
            heapq.heapreplace(heap, i.end)
        else:
            # a new room is allocated
            heapq.heappush(heap, i.end)
    return len(heap)
  
"""
greedy: 前面释放出来的room还可以被后面的再用，要考虑这一点，简单的sort cannot solve the problem
Arranging the meetings according to their start times helps us know the natural order of 
meetings throughout the day. However, simply knowing when a meeting starts doesn't tell us 
much about its duration.
We also need the meetings sorted by their ending times because an ending event essentially 
tells us that there must have been a corresponding starting event and more importantly, an 
ending event tell us that a previously occupied room has now become free.
When we encounter an ending event, that means that some meeting that started earlier has ended now. 
We are not really concerned with which meeting has ended. All we need is that some meeting ended thus 
making a room available.
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms
    
# https://www.youtube.com/watch?v=FdzJmTCVyJU&t=275s
# time complexity: O(nlogn)
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res


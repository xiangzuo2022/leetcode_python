import heapq


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minstack = []
        self.maxstack = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.minstack) == len(self.maxstack):
            heapq.heappush(self.minstack, -
                           heapq.heappushpop(self.maxstack, -num))
        else:
            heapq.heappush(self.maxstack, -
                           heapq.heappushpop(self.minstack, num))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.minstack) == len(self.maxstack):
            return (self.minstack[0] - self.maxstack[0])/2.0
        else:
            return self.minstack[0]


# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()


#https://www.youtube.com/watch?v=itmhHWaHupI
class MedianFinder(object):

    def __init__(self):
        self.small = [] # maxheap
        self.large = [] # minheap   
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -1 * num)
        # make sure every num in small <= every num in large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        else:            
            return (-1 * self.small[0] + self.large[0]) / 2.0 # must be a float 2.0 otherwise cannot pass testcases on leetcode

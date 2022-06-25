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

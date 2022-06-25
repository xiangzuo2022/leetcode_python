from heapq import *

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))#默认是最小堆,最大堆用-num实现
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])



"""
My own solution. 九章视频讲解很好
"""
from heapq import *
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left = []  # min heap
        self.right = []  # max heap
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.left) == len(self.right):
            heappush(self.left,-heappushpop(self.right,-num))
        else:
            heappush(self.right,-heappushpop(self.left,num))
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.left) == len(self.right):
            return float(self.left[0] - self.right[0])/2.0
        else:
            return float(self.left[0])

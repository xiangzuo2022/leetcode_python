
"""
jiuzhang 模板 binary search O(logn)
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0; right = n
        while left+1 < right:
            m = (left+right)/2
            if isBadVersion(m):
                right = m
            else:
                left = m
        if isBadVersion(left):
            return left
        return right
        
"""
My own solution
"""
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left)/2
            if isBadVersion(mid) is True:
                right = mid - 1
            elif isBadVersion(mid) is False:
                left = mid + 1
        return left

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return n
        start, end = 0, n
        while start + 1 < end:
            mid = start + (end - start)/2
            if isBadVersion(mid) == True:
                end = mid
            else:
                start = mid
            
        if isBadVersion(start): return start
        if isBadVersion(end): return end
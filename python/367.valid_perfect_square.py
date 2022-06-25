"""
binary search
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        left, right = 0, num
        while left <= right:
            mid = left + (right - left)/2
            if mid ** 2 == num:
                return True
            elif mid**2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

"""
Newton's method
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r*r > num:
            r = (r + num/r)/2
        return r*r == num

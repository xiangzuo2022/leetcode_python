"""
a video: https://www.youtube.com/watch?v=ha8RA6ZpRyY
"""
class Solution(object):
    def maxLength(self, ribbons, k):
        """
        :type ribbons: List[int]
        :type k: int
        :rtype: int
        """
        l = 1
        r = max(ribbons)
        while l <= r:
            mid = (l+r)//2
            if self.can_cut(ribbons, k, mid):
                l = mid + 1
            else:
                r = mid - 1

        return r 
    
    def can_cut(self, ribbons, k, length):
        cut = 0
        for ribbon in ribbons:
            cut += ribbon // length 
        return cut >= k 
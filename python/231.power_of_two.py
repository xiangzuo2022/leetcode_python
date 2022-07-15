class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        if n == 1: return True
        
        while n > 1:
            if n % 2 == 0:
                n = n /2
            else:
                return False
        return True
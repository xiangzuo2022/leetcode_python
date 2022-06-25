# O(n)
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        i = 0
        while True:
            sum += i
            if sum + i >= n:
                break
            else:
                i += 1
        return i

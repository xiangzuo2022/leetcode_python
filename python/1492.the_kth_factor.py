"""
方法一：枚举
我们可以从小到大枚举所有在 [1, n] 范围内的数，并判断是否为 n 的因子。
"""
class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        count = 0
        for factor in range(1, n+1):
            if n % factor == 0:
                count += 1
                if count == k:
                    return factor
        return -1
      
"""
不是特别明白的解法二
"""
class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
       
  
        count = 0
        factor = 1
        while factor * factor <= n:
            if n % factor == 0:
                count += 1
                if count == k:
                    return factor
            factor += 1
        factor -= 1
        if factor * factor == n:
            factor -= 1
        while factor > 0:
            if n % factor == 0:
                count += 1
                if count == k:
                    return n // factor
            factor -= 1
        return -1
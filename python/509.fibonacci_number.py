"""
DP
https://www.youtube.com/watch?v=mBNrRy2_hVs&t=13s
"""
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: 
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]  
      
      
"""
recursion
"""
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        return self.fib(n-1) + self.fib(n-2)


"""
 more than two adjacent fence posts have the same color, not ONE.
 这道题就是一个最优解问题，很明显应该采用动规。dp[i]是涂到第i个fence时方法的总数，只和前两个fence的颜色方案有关。以三个栅栏为例，
 栅栏1有k种颜色可选，栅栏2亦然，栅栏3则要看前两个栅栏，1和2的颜色是否相同。如果3和2可以相同，那么必定和1不同，这种情况3有k-1种方案；
 如果3和2不可以相同，那么说明1和2相同，所以3也只有k-1种方案。
"""
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return k

        dp = [0] * n
        dp[0] = k
        dp[1] = k * k
        for i in range(2, n):
            dp[i] = (dp[i - 1] + dp[i - 2]) * (k - 1)
        return dp[n - 1]
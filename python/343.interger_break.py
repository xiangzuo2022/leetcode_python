"""
dp[i]：分拆数字i，可以得到的最大乘积为dp[i]。
动规五部曲，分析如下：
确定dp数组（dp table）以及下标的含义
dp[i]：分拆数字i，可以得到的最大乘积为dp[i]。
dp[i]的定义讲贯彻整个解题过程，下面哪一步想不懂了，就想想dp[i]究竟表示的是啥！
确定递推公式
可以想 dp[i]最大乘积是怎么得到的呢？
其实可以从1遍历j，然后有两种渠道得到dp[i].
一个是j * (i - j) 直接相乘。
一个是j * dp[i - j]，相当于是拆分(i - j)，对这个拆分不理解的话，可以回想dp数组的定义。
"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i-1):            
                dp[i] = max(dp[i], max(j*(i - j), j*dp[i - j]))
        return dp[n]
        
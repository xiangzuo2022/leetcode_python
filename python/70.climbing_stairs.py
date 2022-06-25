class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
    	
    	dp = [1] * (n+1)
    	for i in range(2,n+1):
    		dp[i] = dp[i-1] + dp[i-2]
    	return dp[n]



# ********** The Second Time********
"""
# Solution: 这道题就是经典的讲解最简单的DP问题的问题。。
# 假设梯子有n层，那么如何爬到第n层呢，因为每次只能怕1或2步，那么爬到第n层的方法要么是从第n-1层一步上来的，
# 要不就是从n-2层2步上来的，所以递推公式非常容易的就得出了：
#dp[n] = dp[n-1] + dp[n-2]
"""
class Solution:
    # @param {integer} n
    # @return {integer}
     def climbStairs(self, n):
        dp = [1]*(n+1)
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

"""
另一种写法， 思路是一样的
方法三：动态规划
算法

不难发现，这个问题可以被分解为一些包含最优子结构的子问题，即它的最优解可以从其子问题的最优解来有效地构建，我们可以使用动态规划来解决这一问题。

第 i 阶可以由以下两种方法得到：

在第 (i-1) 阶后向上爬一阶。

在第 (i-2) 阶后向上爬 22 阶。

所以到达第 i 阶的方法总数就是到第 (i-1) 阶和第 (i-2) 阶的方法数之和。

令 dp[i] 表示能到达第 i 阶的方法总数：

dp[i]=dp[i-1]+dp[i-2]

"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for i in range(n)]  #初始化全为1
        for i in range(1,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]




"""
DP solution
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [0] * n
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        steps[0] = 1
        steps[1] = 2
        for i in range(2, n):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n-1]






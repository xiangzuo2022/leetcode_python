"""
# Solution: 解题思路：这道题和climbing stairs很像，可以用动态规划解决。
# 状态转移方程为dp[i][j]=dp[i-1][j]+dp[i][j-1]。
# 使用二维数组来实现, 规律为除了第一行和第一列全为1外，其他格的路径数为其上一格和左一格的和。
# d[i][j] 表示最后一个格子时的状态， 然后看它的前一个状态
"""

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
    	if m == 1 and n == 1:
    		dp = [[1]]
    	elif m == 1 and n > 1:
    		dp = [[1 for i in range(n)]]  # notice the differences
    	elif m > 1 and n == 1:
    		dp = [[1] for i in range(m)]  # notice the differences
    	else:
	    	dp = [[0 for i in range(n)] for i in range(m)]
	    	for i in range(0,n):
	    		dp[0][i] = 1

	    	for i in range(0,m):
	    		dp[i][0] = 1

	    	for i in range(1,m):
	    		for j in range(1,n):
	    			dp[i][j] = dp[i-1][j] + dp[i][j-1]
    	return dp[m-1][n-1]


# 自己写的一次性accept
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]

## cleaner code
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [[0 for j in range(n)] for i in range(m)]
        f[0][0] = 1 
        
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 or j == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = f[i][j-1] + f[i-1][j]
        return f[m-1][n-1]


         
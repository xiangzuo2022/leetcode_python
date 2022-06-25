"""
# 遇到障碍值为0， 其他和62题一样。
dp[i][j] 表示到（i,j）时的所有可能路径之和， 从后往前看
"""


class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        
        m = len(obstacleGrid); n = len(obstacleGrid[0]) # get m and n
        dp = [[0 for i in range(n)] for j in range(m)] # initilization

        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:                
                break   # 有一个障碍， 整条路不能走了, 这一段判断很重要

        for i in range(n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1: 
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
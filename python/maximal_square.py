class Solution:
    # @param {character[][]} matrix
    # @return {integer}
     def maximalSquare(self, matrix):
        if matrix == []:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for x in range(m)]
        ans = 0
        for x in range(m):
            for y in range(n):
                dp[x][y] = int(matrix[x][y])
                if x and y and dp[x][y]:
                    dp[x][y] = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]) + 1 
                ans = max(ans, dp[x][y])
        return ans * ans

# [x][y] is the upper right point


#  ********** The Second Time ********
"""
# DP
# dp[x][y]表示以坐标(x, y)为右下角元素的全1正方形矩阵的最大长度（宽度）
jiuzhang视频强化班思路讲得很好
"""


class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if matrix == []: return 0
        m = len(matrix); n = len(matrix[0])
        dp = [[0]*n for x in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                dp[i][j] = int(matrix[i][j]) # matrix 是string类型的
                if i and j and dp[i][j]: # 省去了判断i,j的范围
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1 # square should be the smallest one
                ans = max(ans, dp[i][j])
        return ans * ans





















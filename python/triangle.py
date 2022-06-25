"""
# 解题思路：使用动态规划（dp）。需要注意的是从后往前更新！
dp[i]的含义是从顶端走到当前行dp[i]这个位置的最小路径和。
水中的鱼的思路：一维DP。逐行扫描，每一个位置能取得的最小sum，是该元素上面两个能取得的最小sum中最小的那一个
sum加上自己的值。只需要开一个数组重复利用就行了。实现的时候，有些繁琐的地方，这个题比较好从下往上扫描。
如果从上往下，其中minV的初始值问题就很头疼。
"""

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 0: 
            return 0
        dp = [0 for i in range(len(triangle))]  # initilization
        dp[0] = triangle[0][0]

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i]) - 1, -1, -1):
                if j == len(triangle[i]) - 1:  # 处理两个极端cases
                    dp[j] = dp[j-1] + triangle[i][j]
                elif j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + triangle[i][j] 
        return min(dp)  






# ************ The Second Time *****************
"""
from the bottom to the up
"""
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        for i in range(len(triangle)-2,-1,-1): # begins from the last row 
            for j in range(0,i+1):  # each row has i elements
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1]) # current line equals the bottom line's result
        return triangle[0][0]


"""
九章solution
"""
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [[0 for i in range(n)] for i in range(n)]
        # 初始化
        for i in range(n):
            dp[n-1][i] = triangle[n-1][i] #最后一行

        for i in range(n-2,-1,-1):# 从倒数第二行开始
            for j in range(0,i+1):
                dp[i][j] = min(dp[i+1][j],dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]




























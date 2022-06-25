"""
完全背包，find组合不是排列
"""

class Solution:
    def numSquares(self, n: int) -> int:
        # 初始化
        # 组成和的完全平方数的最多个数，就是只用1构成
        # 因此，dp[i] = i
        dp = [i for i in range(n + 1)]
        # dp[0] = 0 无意义，只是为了方便记录特殊情况:
        # n本身就是完全平方数，dp[n] = min(dp[n], dp[n - n] + 1) = 1

        for i in range(1, n): # 遍历物品
            if i * i > n:
                break
            num = i * i
            for j in range(num, n + 1): # 遍历背包
                dp[j] = min(dp[j], dp[j - num] + 1)

        return dp[n]
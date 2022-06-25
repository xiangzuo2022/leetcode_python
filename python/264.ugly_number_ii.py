思路二：动态规划

dp[i] 表示第i个丑数

那么dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])

这里 l_2, l_3, l_5是表示，指到的位置。

时间复杂度：O(n)O(n)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        l_2 = 0
        l_3 = 0
        l_5 = 0
        for i in range(1, n):
            dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])
            if dp[i] >= 2 * dp[l_2]:
                l_2 += 1
            if dp[i] >= 3 * dp[l_3]:
                l_3 += 1
            if dp[i] >= 5 * dp[l_5]:
                l_5 += 1
        return dp[-1]

作者：powcai
链接：https://leetcode-cn.com/problems/ugly-number-ii/solution/dui-he-dong-tai-gui-hua-by-powcai/

"""
解释的非常好： https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-han-sh-rzlz/
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]


作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-han-sh-rzlz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
注意到在状态转移方程中，dp[i][0]\textit{dp}[i][0]dp[i][0] 和 dp[i][1]\textit{dp}[i][1]dp[i][1] 只会从 dp[i−1][0]\textit{dp}[i-1][0]dp[i−1][0] 和 dp[i−1][1]\textit{dp}[i-1][1]dp[i−1][1] 转移而来，因此我们不必使用数组存储所有的状态，而是使用两个变量 sell\textit{sell}sell 以及 buy\textit{buy}buy 分别表示 dp[..][0]\textit{dp}[..][0]dp[..][0] 和 dp[..][1]\textit{dp}[..][1]dp[..][1] 直接进行状态转移即可。
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sell, buy = 0, -prices[0]
        for i in range(1, n):
            sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
        return sell


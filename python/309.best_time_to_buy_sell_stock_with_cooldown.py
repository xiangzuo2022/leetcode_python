
"""
引入辅助数组sells和buys

sells[i]表示在第i天卖出股票所能获得的最大累积收益
buys[i]表示在第i天买入股票所能获得的最大累积收益

初始化令sells[0] = 0，buys[0] = -prices[0]
第i天交易时获得的累计收益只与第i-1天与第i-2天有关

记第i天与第i-1天的价格差：delta = price[i] - price[i - 1]

状态转移方程为：

sells[i] = max(buys[i - 1] + prices[i], sells[i - 1] + delta) 
buys[i] = max(sells[i - 2] - prices[i], buys[i - 1] - delta)
上述方程的含义为：

第i天卖出的最大累积收益 = max(第i-1天买入~第i天卖出的最大累积收益, 第i-1天卖出后反悔~改为第i天卖出的最大累积收益)
第i天买入的最大累积收益 = max(第i-2天卖出~第i天买入的最大累积收益, 第i-1天买入后反悔~改为第i天买入的最大累积收益)
而实际上：

第i-1天卖出后反悔，改为第i天卖出 等价于 第i-1天持有股票，第i天再卖出
第i-1天买入后反悔，改为第i天买入 等价于 第i-1天没有股票，第i天再买入
所求的最大收益为max(sells)。显然，卖出股票时才可能获得收益。
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        buys = [0]*n
        sells = [0]*n
        dp = [0] * n
        sells[0] = 0
        buys[0] = -prices[0]
        for i in range(1, n):
            delta = prices[i] - prices[i-1]
            sells[i] = max(buys[i-1] + prices[i], sells[i-1] + delta)
            buys[i] = max(buys[i-1] - delta, sells[i-2] - prices[i])
        return max(sells)



维持两个数组，having数组和notHaving数组，分别表示那一天是持有还是不持有获得的最大收益持有状态，可以由两种状态导致：

第i-1天持有，第i天仍然仍然持有i-2不持有，第i天买入 （这里i-2为了满足冷冻期）不持有状态，也可以由两种状态导致：
i-1不持有，第i天仍然不持有i-1持有，第i天卖掉状态转移方程：

having[i]=max(notHaving[i-2]-prices[i],having[i-1])
notHaving[i]=max(having[i-1]+prices[i],notHaving[i-1])

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/dong-tai-gui-hua-python-by-juncao8101/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n<=1:
            return 0
        if n==2:
            count=prices[1]-prices[0]
            return count if count>0 else 0
        notHaving=n*[0]
        having=n*[0]
        having[0]=-prices[0]
        having[1]=max(notHaving[0]-prices[1],having[0])
        notHaving[1]=max(having[0]+prices[1],notHaving[0])
        for i in range(2,n):
            having[i]=max(notHaving[i-2]-prices[i],having[i-1])
            notHaving[i]=max(having[i-1]+prices[i],notHaving[i-1])
        return max(having[-1],notHaving[-1])

"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/zui-jia-mai-mai-gu-piao-shi-ji-han-leng-dong-qi-4/
方法一：动态规划
思路与算法:
我们用 f[i]f[i]f[i] 表示第 iii 天结束之后的「累计最大收益」。根据题目描述，由于我们最多只能同时买入（持有）一支股票，并且卖出股票后有冷冻期的限制，
因此我们会有三种不同的状态：
我们目前持有一支股票，对应的「累计最大收益」记为 f[i][0]f[i][0]f[i][0]；
我们目前不持有任何股票，并且处于冷冻期中，对应的「累计最大收益」记为 f[i][1]f[i][1]f[i][1]；
我们目前不持有任何股票，并且不处于冷冻期中，对应的「累计最大收益」记为 f[i][2]f[i][2]f[i][2]。
这里的「处于冷冻期」指的是在第 iii 天结束之后的状态。也就是说：如果第 iii 天结束之后处于冷冻期，那么第 i+1i+1i+1 天无法买入股票。
如何进行状态转移呢？在第 iii 天时，我们可以在不违反规则的前提下进行「买入」或者「卖出」操作，此时第 iii 天的状态会从第 i−1i-1i−1 天的状态转移而来；
我们也可以不进行任何操作，此时第 iii 天的状态就等同于第 i−1i-1i−1 天的状态。那么我们分别对这三种状态进行分析：
对于 f[i][0]f[i][0]f[i][0]，我们目前持有的这一支股票可以是在第 i−1i-1i−1 天就已经持有的，对应的状态为 f[i−1][0]f[i-1][0]f[i−1][0]；
或者是第 iii 天买入的，那么第 i−1i-1i−1 天就不能持有股票并且不处于冷冻期中，对应的状态为 f[i−1][2]f[i-1][2]f[i−1][2] 加上买入股票的负收益 
prices[i]{\it prices}[i]prices[i]。因此状态转移方程为：
f[i][0]=max(f[i−1][0],f[i−1][2]−prices[i])f[i][0] = \max(f[i-1][0], f[i-1][2] - {\it prices}[i])
f[i][0]=max(f[i−1][0],f[i−1][2]−prices[i])
对于 f[i][1]f[i][1]f[i][1]，我们在第 iii 天结束之后处于冷冻期的原因是在当天卖出了股票，那么说明在第 i−1i-1i−1 天时我们必须持有一支股票，
对应的状态为 f[i−1][0]f[i-1][0]f[i−1][0] 加上卖出股票的正收益 prices[i]{\it prices}[i]prices[i]。因此状态转移方程为：

f[i][1]=f[i−1][0]+prices[i]f[i][1] = f[i-1][0] + {\it prices}[i]
f[i][1]=f[i−1][0]+prices[i]

对于 f[i][2]f[i][2]f[i][2]，我们在第 iii 天结束之后不持有任何股票并且不处于冷冻期，说明当天没有进行任何操作，即第 i−1i-1i−1 天时不持有任何股票：如果处于冷冻期，对应的状态为 f[i−1][1]f[i-1][1]f[i−1][1]；如果不处于冷冻期，对应的状态为 f[i−1][2]f[i-1][2]f[i−1][2]。因此状态转移方程为：

f[i][2]=max(f[i−1][1],f[i−1][2])f[i][2] = \max(f[i-1][1], f[i-1][2])
f[i][2]=max(f[i−1][1],f[i−1][2])

这样我们就得到了所有的状态转移方程。如果一共有 nnn 天，那么最终的答案即为：

max(f[n−1][0],f[n−1][1],f[n−1][2])\max(f[n-1][0], f[n-1][1], f[n-1][2])
max(f[n−1][0],f[n−1][1],f[n−1][2])

注意到如果在最后一天（第 n−1n-1n−1 天）结束之后，手上仍然持有股票，那么显然是没有任何意义的。因此更加精确地，最终的答案实际上是 f[n−1][1]f[n-1][1]f[n−1][1] 和 f[n−1][2]f[n-1][2]f[n−1][2] 中的较大值，即：

max(f[n−1][1],f[n−1][2])\max(f[n-1][1], f[n-1][2])
max(f[n−1][1],f[n−1][2])

细节

我们可以将第 000 天的情况作为动态规划中的边界条件：

⎧⎩⎨⎪⎪f[0][0]f[0][1]f[0][2]=−prices[0]=0=0\begin{cases}f[0][0] &= -{\it prices}[0] \\f[0][1] &= 0 \\f[0][2] &= 0\end{cases}
⎩
⎪
⎪
⎨
⎪
⎪
⎧
​
  
f[0][0]
f[0][1]
f[0][2]
​
  
=−prices[0]
=0
=0
​
 

在第 000 天时，如果持有股票，那么只能是在第 000 天买入的，对应负收益 −prices[0]-{\it prices}[0]−prices[0]；如果不持有股票，那么收益为零。注意到第 000 天实际上是不存在处于冷冻期的情况的，但我们仍然可以将对应的状态 f[0][1]f[0][1]f[0][1] 置为零，这其中的原因留给读者进行思考。

这样我们就可以从第 111 天开始，根据上面的状态转移方程进行进行动态规划，直到计算出第 n−1n-1n−1 天的结果。
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            f[i][1] = f[i - 1][0] + prices[i]
            f[i][2] = max(f[i - 1][1], f[i - 1][2])
        
        return max(f[n - 1][1], f[n - 1][2])

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/zui-jia-mai-mai-gu-piao-shi-ji-han-leng-dong-qi-4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
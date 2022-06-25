# 解题思路：只允许做两次交易，这道题就比前两道要难多了。解法很巧妙，有点动态规划的意思：开辟两个
# 数组f1和f2，f1[i]表示在price[i]之前进行一次交易所获得的最大利润，f2[i]表示在price[i]之后
# 进行一次交易所获得的最大利润。则f1[i]+f2[i]的最大值就是所要求的最大值，而f1[i]和f2[i]的计算就需
# 要动态规划了，看代码不难理解。如果进行两次transaction, 顺序只能是买入->卖出->买入->卖出.

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
    	n = len(prices)
    	if n == 0:return 0
    	f1 = [0 for i in range(n)]
    	f2 = [0 for i in range(n)]
    	minvalue = prices[0]
    	for i in range(1,n):
    		minvalue = min(minvalue,prices[i])
    		f[i] = max(f[i-1],prices[i] - minvalue)

    	maxvalue = prices[n-1]
    	for i in range(n-2,-1,-1):
    		maxvalue = max(maxvalue,prices[i])
    		f2[i] = max(f2[i+1],maxvalue-prices[i])
    	res = 0
    	for i in range(n):
    		res = max(res,f1[i]+f2[i]) 
    	return res


"""
jiuzhang solution
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 1:
            return 0
        left = prices[:]; right = prices[:]; n = len(prices);profit = 0
        
        left[0] = 0; min_value = prices[0]
        for i in range(1,n):
            min_value = min(min_value,prices[i])
            left[i] = max(left[i-1],prices[i] - min_value)
            
        right[n-1] = 0;max_value = prices[n-1]
        for i in range(n-2,-1,-1):
            max_value = max(max_value,prices[i])
            right[i] = max(right[i+1],max_value-prices[i])
            
        for i in range(n):
            profit = max(profit, left[i]+right[i])
        return profit


"""
Solution with DP
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
        f1 = [0]*n
        f2 = [0]*n
        minvalue = prices[0]
        for i in range(1, n):
            minvalue = min(minvalue, prices[i])
            f1[i] = max(prices[i] - minvalue, f1[i-1])

        maxvalue = prices[n-1]
        for i in range(n-2, -1, -1): # don't know where is the last transaction ending point, so from the end to the front search for the 2nd max value
            maxvalue = max(maxvalue, prices[i])
            f2[i] = max(maxvalue - prices[i], f2[i+1])

        ans = 0
        for i in range(n):
            ans = max(ans, f1[i] + f2[i])
        return ans
            
"""
https://github.com/emilyzuo2021/leetcode-master/blob/master/problems/0123.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIII.md
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        dp = [0] * 5 
        dp[1] = -prices[0]
        dp[3] = -prices[0]
        for i in range(1, len(prices)):
            dp[1] = max(dp[1], dp[0] - prices[i])
            dp[2] = max(dp[2], dp[1] + prices[i])
            dp[3] = max(dp[3], dp[2] - prices[i])
            dp[4] = max(dp[4], dp[3] + prices[i])
        return dp[4]
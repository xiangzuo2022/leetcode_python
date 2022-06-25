# use DP
# 由于直接采用动态规划会返回Time Limit Exceeded，可以针对题目部分样例做出下面的优化：
# 令最大交易次数为k，数组长度为size；则当k > size / 2时，问题可以转化为：Best Time to Buy and Sell Stock II

class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
    	size = len(prices)
    	if k > size/2:
    		return self.quickSolve(size,prices)
    	else:
    		dp = [None]*(2*k+1)
    		dp[0] = 0
    		for i in range(size):
    			for j in range(min(2*k,i+1),0,-1): # dp一般是从后向前
    				dp[j] = max(dp[j],dp[j-1]+prices[i]*[1,-1][j%2])
    	return max(dp)


    def quickSolve(self,size,prices):
    	sums = 0
    	for x in range(size-1):
    		if prices[x+1] > prices[x]:
    			sums += prices[x+1] - prices[x]
    	return sums


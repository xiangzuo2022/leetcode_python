
"""
解题思路：由于可以进行无限次的交易，那么只要是递增序列，就可以进行利润的累加。
"""
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
    	maxprofit = 0
    	for i in range(1,len(prices)):
    		if prices[i] > prices[i-1]:
    			maxProfit += prices[i] - prices[i-1]
    	return maxprofit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        n = len(prices)
        for i in range(n-1):
            if prices[i+1] > prices[i]:
                maxprofit += prices[i+1] - prices[i]
        return maxprofit


#  My own soluton
class Solution(object):
def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n <= 1:return 0
    maxProfit = 0;low = prices[0]
    for i in range(n):
        if prices[i] < low:                
            low = prices[i]
        maxProfit += prices[i] - low
        low = prices[i]
    return maxProfit
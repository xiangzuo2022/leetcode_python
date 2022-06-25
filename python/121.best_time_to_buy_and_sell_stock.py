class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
    	if len(prices) <= 1:
    		return 0
    	low = prices[0]
    	maxProfit = 0

    	for i in range(len(prices)):
    		if prices[i] < low:
    			low = prices[i]
    		maxProfit = max(prices[i] - low , maxProfit)
    	return maxProfit


"""
subarray的思想prefix sum, 但要注意初始化
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:return 0
        profit = 0;min_value = prices[0]
        for i in range(len(prices)):
            min_value = min(min_value,prices[i])
            profit = max(profit,prices[i]-min_value)            
        return profit


"""
my own DP solution and need to think about how many variables needs to be maintained. Here only one, profit. 
No need to use opt[] array
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0: return 0
        opt = [0 for i in range(n)]
        opt[0] = 0
        minvalue = prices[0]
        for i in range(1, n):
            minvalue = min(minvalue, prices[i])
            if prices[i] < opt[i - 1]:
                opt[i] = prices[i]
            else:
                opt[i] = max(prices[i] - minvalue, opt[i - 1]) # select or not select the i-th element

        return max(opt)
      
"""
my own solution: maintain a minvalue and also a maxvalue. Keep updating these two values
"""      
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        minValue = prices[0]
        n = len(prices)
        maxProfit = -sys.maxint
        for i in range(n):
            minValue = min(minValue, prices[i])            
            maxProfit = max(prices[i] - minValue, maxProfit)          
        return maxProfit
# 以下解法ML

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
    	if n == 0: return 0
    	subString = ''
    	for i in range(1,n+1):
    		subString += 'i'
    	count = 0
    	for i in range(len(subString)):
    		if subString[i] == '1':
    			count += 1
    	return count

# 一下是新解法， 但看不懂 
# https://leetcode.com/discuss/44281/4-lines-o-log-n-c-java-python
# http://blog.csdn.net/xudli/article/details/46798619

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n/m + 8) / 10 * m + (n/m % 10 == 1) * (n%m + 1)
            m *= 10
        return ones
        

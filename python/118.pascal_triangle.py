"""初始化数组a的方法可以解决“1”的问题
	此题考查二维数组的操作
"""

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
    	a = [[1]* (i+1) for i in range(numRows)]    	
    	for i in range(numRows):    			
	        for j in range(1,  i):	        	
	           	a[i][j] = a[i-1][j-1] + a[i-1][j]
	           	
	return a


if __name__ == '__main__':
	b = Solution()
	print b.generate(0)
"""
此解法是数学意义的， 只能记忆了
"""

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
    	res = []
    	size = 1<<n # equals to 2^n
         	
    	for i in range(size):
            print i 
            res.append((i>>1)^i)  # ^ is xor
    	return res

if __name__ == '__main__':
	a = Solution()
	a.grayCode(4)
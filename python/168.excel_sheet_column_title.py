class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
    	# chr() translates number into character
    	# ord() translates character into number

    	d = {i+1:chr(ord('A')+i) for i in range(26)}
    	r= ''

    	while n > 0:
        	l = n % 26 or 26        	
        	r = d[l] + r        	
        	n = (n-l) / 26  
    	return r

"""
The Third Time
"""
class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        ans = ''
        while n:
            ans = chr(ord('A') + (n-1) % 26) + ans # ans 放在后面加， 要不然结果是相反的
            n = (n - 1) / 26
        return ans
    	
    	
   

    	

if __name__ == '__main__':
	a = Solution()
	print a.convertToTitle(52)
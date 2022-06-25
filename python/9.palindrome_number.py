class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
    	
    	return str(x)==str(x)[::-1]

if __name__ == '__main__':
	a = Solution()
	print a.isPalindrome(121)

# 回文是正反读都一样
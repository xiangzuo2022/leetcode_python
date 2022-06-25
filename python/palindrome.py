class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
    	return str(x) == str(x)[::-1]
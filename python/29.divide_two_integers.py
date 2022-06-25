"""
# 解题思路：不许用乘、除和求余实现两数的相除。那就只能用加和减了。正常思路是被除数一个一个的减除数，
# 直到剩下的数比除数小为止，就得到了结果。这样是无法ac的，因为时间复杂度为O(n)，比如一个很大的数除1，
# 就很慢。这里我们可以用二分查找的思路，可以说又是二分查找的变种。
# 除法不用关心余数， 只关心商
"""


class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
    	if abs(dividend) < abs(divisor):
    		return 0
    	sums = 0; count = 0 ; res = 0
    	a = abs(dividend); b = abs(divisor)
    	while a >= b:
    		sums = b
    		count = 1
    		while sums + sums <= a:
    			sums += sums
    			count += count
    		a -= sums  # 减去的sums已经是可以除尽的了
    		res += count
    	if divisor*dividend < 0:
    		res = -1*res
            return max(-2147483648,res)
        else:
            return min(res,2147483647)






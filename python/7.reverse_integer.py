class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
    	ans = 0    	
    	if x > 0:
    		sign = 1
    	else:
    		sign = -1
    	x = abs(x)
    	while x > 0:
    		ans = ans * 10 + x%10
    		x /= 10
    	ans *= sign
    	if ans < -(1<<31) or ans > (1<<31)-1: # overfloat
    		return 0
    	return ans


#[解题思路]
# 如果是用字符串来逆序的话，需要考虑0的特殊性，但是如果直接用一个integer来滚动生成的话，0就不是问题了。
# 当然，溢出的问题是存在的，所以return -1。


"""
忘记了判断溢出情况， 注意溢出的两个边界 ans < -(1<<31) or ans > (1<<31)-1
以下解法先把int转为str，让后利用string的逆序
"""
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        sign = 1
        if x < 0:
            x =abs(x)
            sign = -1
        x = str(x)
        x = x[::-1]
        y = sign * int(x)
        if y < -(1<<31) or y > (1<<31)-1:
            return 0
        else:
            return y

"""
反转的另一种写法
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            x = abs(x)
            sign = -1
        x = list(str(x))
        i = 0; j = len(x)-1
        while i < j :
            x[i],x[j] = x[j],x[i]
            i += 1
            j -= 1
        x = sign * int(''.join(x))
        if -1<<31 < x < (1<<31)-1:
            return x
        else:
            return 0



"""
整数滚动的方法很妙
"""
class Solution:
    # @param {integer} x
    # @return {integer}
     def reverse(self, x):
        sign = 1
        ans = 0
        if x < 0:
            x =abs(x)
            sign = -1
            
        while x > 0:          
            ans = ans*10 + x % 10
            x = x/10        
        ans = sign * ans
        if ans < -(1<<31) or ans > (1<<31)-1:
            return 0
        else:
            return ans

"""Summary:一旦涉及到int就要考虑溢出
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31-1
        ans = 0
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
            
        while x > 0:            
            ans = ans*10 + x%10
            x =x/10
        ans *= sign
        if ans < INT_MIN or ans > INT_MAX:
            return 0
        
        return ans









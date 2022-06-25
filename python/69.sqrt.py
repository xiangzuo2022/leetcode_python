"""
Newton's method
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r*r > x:
            r = (r + x/r)/2
        return r



class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
    	if x == 0:
    		return 0
    	i = 1; j = x/2 + 1
    	while (i <= j):
    		mid = (i + j)/2
    		if mid ** 2 == x:
    			return mid
    		elif mid ** 2 > x:
    			j = mid - 1
    		elif mid ** 2 < x:
    			i = mid + 1
    	return j  # ?? why return j


# ******* The Second Time ********
# math problem
# 解法一 runtime error
class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 0: return 0
        for i in range(1,x):
            if i*i == x:
                return i 

"""
# 解法二：清晰易懂 I like it
# 解题思路：实现开平方函数。这里要注意的一点是返回的是一个整数。通过这一点我们可以看出，很有可能是使用二
# 分查找来解决问题的。这里要注意折半查找起点和终点的设置。起点i=1；终点j=x/2+1；因为在(x/2+1)^2 > x，
# 所以我们将折半查找的终点设为x/2+1。
# 奇葩的是不考虑溢出也能AC。最好还是考虑吧
"""

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        left = 0; right = 46340  # sqrt(C MAX_INT 2147483647)=46340.950001
        # right = x/2 + 1
        while left <= right:
            mid = (left + right) /2
            if mid**2 <= x < (mid+1)**2:  # 要稍微放一点
                return mid
            elif x < mid**2:
                right = mid - 1
            else:
                left = mid + 1



                    
































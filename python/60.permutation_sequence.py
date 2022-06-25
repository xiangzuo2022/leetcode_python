"""
# 我采用的方法是计算第k个Permutation。 假设n = 6，k = 400, 先计算第一位，
# 第一位为6，那么它最少也是第5! * 5 + 1个排列，这是因为第一位为1/2/3/4/5时，都有5!个排列，因此第一
# 位为6时，至少是第5! * 5 + 1个排列（这个排列为612345）。5! * 5 + 1 = 601 > k，所以第一位不可能是6.
# 一个一个地枚举，直到第一位为4时才行，这时，4xxxxx至少为第5! * 3 + 1 = 361个排列。
# 然后计算第二位，与计算第一位时的区别在于，46xxxx至少为第4! * 4 + 1 = 97个排列，这是因为比6小的只
# 有5/3/2/1了。最后可以计算出第二位为2。
"""

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k): # k是第几个排列
    	res = ''
    	k -= 1
    	fac = 1
    	for i in range(1,n):
    		fac * = i  # for （n-1）! 
    	num = [i for i in xrange(1,n+1)]
    	for i in reversed(xrange(n)):
    		curr = num[k/fac]
    		res += str(curr)
    		num.remove(curr) # 不移去会有重复元素出现
    		if i != 0:
    			k %= fac
    			fac /= i  # e.g., (n-1)!/(n-1) = (n-2)!
    	return res

    	
# ****************** 以下算法超时 ******************
"""
递归算法超时
"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def dfs(depth,start,value):
           if depth == n:
               ans.append(value)
               return
           for i in range(1,n+1):
               if depth > n :break
               if str(i) not in value:
                dfs(depth+1,i+1,value+str(i))
        
        ans = []
        dfs(0,1,"")
        print ans
        return ans[k-1]








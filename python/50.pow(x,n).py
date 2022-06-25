"""
# 解题思路：求幂函数的实现。使用递归，类似于二分的思路，解法来自Mark Allen Weiss的
# 《数据结构与算法分析》。
# 别忘了考虑n<0的情况
# recursive
"""
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
    	 if n == 0:
    	 	return 1
    	 elif n < 0:
    	 	return 1/ self.myPow(x,-n)
    	 elif n % 2:
    	 	return self.myPow(x*x,n/2)*x # e.g., n = 5 分 odd and even two cases
    	 else:
    	 	return self.pow(x*x,n/2)

"""
official solution:分治的思想
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

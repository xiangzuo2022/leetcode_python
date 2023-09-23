class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, A):
    	max_product = front_max = front_min = A[0]
        for i in xrange(1, len(A)):
            front_max, front_min = max(A[i], A[i]*front_max, A[i]*front_min), min(A[i], A[i]*front_max, A[i]*front_min)
            max_product = max(max_product, front_max, front_min)
        return max_product




"""
# 解题思路：主要需要考虑负负得正这种情况，比如之前的最小值是一个负数，再乘以一个负数就有可能成为一
# 个很大的正数。
此解法最好最直接
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
    	if len(nums)==0: return 0
    	min_tmp = max_tmp = result = nums[0]
    	for i in range(1,len(nums)):
    		a = nums[i] * min_tmp
    		b = nums[i] * max_tmp
    		c = nums[i]
    		max_tmp = max(max(a,b),c)
    		min_tmp = min(min(a,b),c)
    		result = max(max_tmp,result)
    	return result


"""
Solution 2: two tables(DP_max, DP_min) to store the max and min at currenet index i 
by compareing three values(A[i], A[i] * DP_max[-1], A[i] * DP_min[-1]) respectively
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        ps, ns = [nums[0]],[nums[0]]
        for i in range(1,len(nums)):
            tp, np = ps[-1],ns[-1]
            ps.append(max(nums[i],nums[i]*tp,nums[i]*np))
            ns.append(min(nums[i],nums[i]*tp,nums[i]*np))
        return max(ps)


"""
an easy understanding solution
下面这种方法也是用两个变量来表示当前最大值和最小值的，但是没有无脑比较三个数，而是对于当前的nums[i]值进行了正负情况的讨论：
1. 当遍历到一个正数时，此时的最大值等于之前的最大值乘以这个正数和当前正数中的较大值，此时的最小值等于之前的最小值乘以这个正数和当前正数中的较小值。
2. 当遍历到一个负数时，我们先用一个变量t保存之前的最大值mx，然后此时的最大值等于之前最小值乘以这个负数和当前负数中的较大值，
   此时的最小值等于之前保存的最大值t乘以这个负数和当前负数中的较小值。
3. 在每遍历完一个数时，都要更新最终的最大值。
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        mn, mx, res = nums[0], nums[0], nums[0]
        for i in range(1, n):
            if nums[i] > 0:
                mx = max(nums[i], nums[i]*mx)
                mn = min(nums[i], nums[i]*mn)
            else:
                t = mx
                mx = max(nums[i], nums[i]*mn)
                mn = min(nums[i], nums[i]*t)
            res = max(res, mx)
        return res


"""
more concise code
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        mn, mx, res = nums[0], nums[0], nums[0]
        for i in range(1, n):
            if nums[i] < 0:
                mx, mn = mn, mx
            mx = max(nums[i], nums[i]*mx)
            mn = min(nums[i], nums[i]*mn)

            res = max(res, mx)
        return res


"""
good analysis
"""
https://leetcode-cn.com/problems/maximum-product-subarray/solution/si-wei-dao-tu-zheng-li-zui-da-zi-xu-ji-h-r8du/

# https://www.youtube.com/watch?v=lXVy6YWFcRM&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=6
# O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:            
            tmp = curMax * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin * n, n)           
            res = max(res, curMax)
        return res














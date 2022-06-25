# 一下解法不是最好的， 估计有些测试是通不过的
# Negative value cannot be border: This method is based on such a fact that the negative 
# value cannot be the border element in the maximum subarray, since you remove the 
# negative border out, the sum obviously get larger. So we can scan the array from 
# left to right and keep a current sum over the scanned elements. If the current sum 
# become negative, we set it as zero, if the sum is larger than the global maximum sum, 
# We update the maximum sum. To some extent, this is also could be interpreted as DP 
# approach. 

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):

    	current_sum = 0
    	max_sum = -10000

    	for i in range(len(nums)):
    		if current_sum < 0:
    			current_sum = 0
    		current_sum += nums[i]
    		max_sum = max(max_sum,current_sum)

    	return max_sum

"""
#  ********** The Second Time **********
# O(n)的解法
# http://tech-wonderland.net/blog/leetcode-maximum-subarray.html
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
     def maxSubArray(self, A):
        if len(A) == 0: return 0
        temp = 0
        maxSum = A[0]
        for i in range(len(A)):
            temp = max(A[i],A[i]+temp)  # 精华在此是一种动态规划的思想
            if temp > maxSum:
                maxSum = temp
        return maxSum

"""
题目要求的算法：
# O(nlogn): Divide and Conquer: divide the array into left and right part, 
# recursively find the maximum sub array in the left and right parts. 
# The third candidate is the subarray cross the mid element (could be calculated in
# linear time). Then we compare these three result, return the maximum one. 
# The time is T(N) = 2*T(N/2) + O(N), by master’s theroy the time complexity is O(NlogN).
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        return self.maxSubArrayHelper(nums, 0, len(nums) - 1)

    def maxSubArrayHelper(self, nums, l, r):
        if l > r:
            return -2147483647
        #m = l + (r - l) / 2
        m = (l+r)/2
        
        leftMax = sumNum = 0
        for i in range(m - 1, l - 1, -1):
            sumNum += nums[i]
            leftMax = max(leftMax, sumNum)
        
        rightMax = sumNum = 0
        for i in range(m + 1, r + 1):
            sumNum += nums[i]
            rightMax = max(rightMax, sumNum)

        leftAns = self.maxSubArrayHelper(nums, l, m - 1)
        rightAns = self.maxSubArrayHelper(nums, m + 1, r)
            
        return max(leftMax + nums[m] + rightMax, max(leftAns, rightAns))


"""
以下算法不能通过， 是边界问题， 至今没搞明白边界问题
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
       
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.helper(nums,0,len(nums))        
        
    def helper(self,nums,left,right):
        if left > right:return -(1<<32)
        m = (left + right)/2
        leftMax = sums = 0
        for i in range(left,m):
            sums+= nums[i]
            leftMax = max(leftMax,sums)
        
        rightMax = sums = 0
        for i in range(m+1,right):
            sums += nums[i]
            rightMax = max(rightMax,sums)
            
        lm = self.helper(nums,left,m)
        rm = self.helper(nums,m+1,right)
        return max(lm,rm,lm+nums[m]+rm)


"""
九章solution：prefix sum 
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        max_value = -999;sums = 0; min_value = 0
        for i in range(len(nums)):
            sums += nums[i]
            max_value = max(max_value,sums-min_value)
            min_value = min(min_value,sums)
        return max_value


"""
DP solution
f(k)表示以当前元素结尾的子数组的最大值，则f(k)应该等于max(num[k],f(k-1)+num[k])
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i]) # key is here
        return max(dp)

"""
用动态规划的思想是最容易结题的，因为只要一个值, 不要过程
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_value = max_value = nums[0]
        for num in nums[1:]:
          # if the current value + num < num, then abandon the current_value + num and choose the num instead
            curr_value = max(num, curr_value + num)
            max_value = max(max_value, curr_value)
        return max_value



"""
Greedy solution: 遍历nums，从头开始用count累积，如果count一旦加上nums[i]变为负数，那么就应该从nums[i+1]开始从0累积count了，
因为已经变为负数的count，只会拖累总和。
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = -float('inf')
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            if temp > maxSum:
                maxSum = temp
            if temp <= 0:
                temp = 0
        return maxSum
                







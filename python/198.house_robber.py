
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
    	size = len(num)
    	dp = [0] * (size+1)
    	if size:
    		dp[1] = num[0]
    	for i in range(2,size+1):
    		dp[i] = max{dp[i-1],dp[i-2]+num[i-1]}
    	return dp[size]
    		




# ************ The Second Time **********
# Solution: dp[i]表示盗窃i家的最大收益值
# 设动态规划列表 dp ，dp[i] 代表前 i 个房子在满足条件下的能偷窃到的最高金额。
# dp[0] = num[0] （当i=0时）
# dp[1] = max(num[0], num[1]) （当i=1时）
# dp[i] = max(num[i] + dp[i - 2], dp[i - 1]) （当i !=0 and i != 1时）
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[n-1]

"""注意corner cases
"""

"""
jiuzhang solution搞复杂了
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0 for i in range(n)]
        if n == 0:return 0
        if n >= 1:dp[0] = nums[0]
        if n >= 2:dp[1] = max(nums[0],nums[1])
        if n >= 3:dp[2] = max(nums[0]+nums[2],nums[1])
        if n > 2:
            for i in range(3,n):
                dp[i] = max(dp[i-2],dp[i-3]) + nums[i]
        return max(dp)

"""
My own DP solution
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0: return 0
        if n==1: return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]

"""
dp[i]：考虑下标i（包括i）以内的房屋，最多可以偷窃的金额为dp[i]。
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n ==0 : return 0
        if n == 1: return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]
    
# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=47












       


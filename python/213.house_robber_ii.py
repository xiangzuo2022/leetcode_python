class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self.robLinear(nums[1:]), self.robLinear(nums[:-1])) # rob the first room or rob the 
        # last room. If 1st room is chosen then cannot choose the last room. 
        
    # @param num, a list of integer
    # @return an integer
    def robLinear(self, num):
        size = len(num)
        odd, even = 0, 0
        for i in range(size):
            if i % 2:  # the odd case
                odd = max(odd + num[i], even)
            else:  # the even case
                even = max(even + num[i], odd)
        return max(odd, even)


# typical example of circle DP--break the circle into two linear DPs


# ******** The Second Time **********
"""
# House Robber I的升级版. 因为第一个element 和最后一个element不能同时出现. 则分两次
# call House Robber I. case 1: 不包括最后一个element. case 2: 不包括第一个element.
# 两者的最大值即为全局最大值
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]            
        
        def robRange(nums, start, end):
            if start == end:
                return nums[start]
            dp = [0] * len(nums)
            dp[start] = nums[start]
            dp[start+1] = max(nums[start], nums[start+1])
            for i in range(start+2, end+1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[end]
        
        value1 = robRange(nums, 0, n-2)
        value2 = robRange(nums, 1, n-1)
        return max(value1, value2)

"""
解法二：将环形DP问题转化为两趟线性DP问题，可以复用House Robber的代码。另外需要特判一下只有一件房屋的情形。
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self.robLinear(nums[1:]),self.robLinear(nums[:-1]))  # 头和尾只能取其一

    def robLinear(self,nums):
        n = len(nums)
        odd, even = 0,0
        for i in range(n):
            if i % 2 :
                odd = max(odd+nums[i],even)  # 到第i家时的最大值;两种情况， 偷还是不偷， 偷的话是odd + nums[i],
                                            # 不偷的话是even
            else:
                even = max(even+nums[i],odd)
        return max(odd,even)























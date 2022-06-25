"""
compare to 300
概括来说：不连续递增子序列的跟前0-i 个状态有关，连续递增的子序列只跟前一个状态有关
"""

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in range (len(nums)-1):
            if nums[i+1] > nums[i]:
                dp[i+1] = dp[i] + 1
        return max(dp)
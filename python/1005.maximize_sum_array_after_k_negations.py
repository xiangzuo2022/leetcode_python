"""
那么本题的解题步骤为：

第一步：将数组按照绝对值大小从大到小排序，注意要按照绝对值的大小
第二步：从前向后遍历，遇到负数将其变为正数，同时K--
第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
第四步：求和
"""
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
         # 将A按绝对值从大到小排列
        nums = sorted(nums, key=abs, reverse=True)
        for i in range(len(nums)):
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1
        if k > 0:  # 如果K还大于0，那么反复转变数值最小的元素，将K用完; #取A最后一个数只需要写-1
            nums[-1] *=  (-1)**k
        return sum(nums)
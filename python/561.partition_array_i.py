class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        sumValue = 0
        for i in range(n):
            if i % 2 == 0:
                sumValue += nums[i]
        return sumValue


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])

作者：agl66
链接：https://leetcode-cn.com/problems/array-partition-i/solution/python-by-agl66-3/

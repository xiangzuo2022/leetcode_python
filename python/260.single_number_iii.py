"""
jiuzhang 的思想,非常赞！
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for i in range(len(nums)):
            xor ^= nums[i]
        lastBit = xor - (xor&(xor-1))
        group1 = 0; group2 = 0
        for i in range(len(nums)):
            if (lastBit & nums[i]) == 0:
                group1 ^= nums[i]
            else:
                group2^= nums[i]
        return [group1,group2










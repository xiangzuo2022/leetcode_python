"""
蓄水池抽样算法
"""
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = None
        count = 0
        for i, v in enumerate(self.nums):
            if v == target:
                count += 1
                chance = random.randint(1, count)
                if chance == count:
                    res = i
        return res
# sort the array first
# pair element adjecent will give the maximum value


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])  #每隔2个元素
        

"""
思路：用swap，每次从[i,n-1]中随机一个数，和第i个数交换即可。
"""

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        output = self.nums[:]
        n = len(output)
        for i in xrange(n):
            _id = random.randint(i,n-1)
            output[i],output[_id] = output[_id],output[i]
        return output
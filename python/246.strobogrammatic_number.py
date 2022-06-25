"""
这道题定义了一种对称数，就是说一个数字旋转180度和原来一样，也就是倒过来看一样，比如609，倒过来还是609等等，满足这种条件的数字其实没有几个，
只有0,1,8,6,9。这道题其实可以看做求回文数的一种特殊情况，我们还是用双指针来检测，那么首尾两个数字如果相等的话，那么只有它们是0,1,8中间的一个才行，
如果它们不相等的话，必须一个是6一个是9，或者一个是9一个是6，其他所有情况均返回false
"""

class Solution(object):
    def isStrobogrammatic(self, nums):
        """
        :type num: str
        :rtype: bool
        """
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            if nums[l] == nums[r]:
                if nums[l] != '0' and nums[l] != '1' and nums[l] != '8':
                    return False
            else:
                if (nums[l] != '6' or nums[r] != '9') and (nums[l] != '9' or nums[r] != '6'):
                    return False
            l += 1
            r -= 1
        return True
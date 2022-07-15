"""
即当两个数除以某个数的余数相等，那么二者相减后肯定可以被该数整除。同余定理：
a good video to explain it. 
https://www.bilibili.com/video/BV1UV411x7jw?spm_id_from=333.337.search-card.all.click
"""
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {0: -1}
        pre = 0
        for index, num in enumerate(nums):
            pre += num
            rem = pre % k
            i = d.get(rem, index)
            if i == index:
                d[rem] = index
            elif index - i >= 2:
                return True
        return False
"""
题目给了那么多限制条件，应该也能想得出二分查找的方法。思路是我们在[1,N]范围内先求出mid，再统计小于等于mid的数字个数count，
如果count<=mid，说明重复数字在[mid+1,N]中，否则在[1,mid)中。
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + (right - left)/2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            if count > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left

"""
重点概括：
题目要找的是一个 整数，这个整数有明确的范围（11 到 nn） 之前，因此可以使用「二分查找」；
每一次猜一个数，然后 遍历整个输入数组，进而缩小搜索区间，最后确定重复的是哪个数；
不是在「输入数组」上直接使用「二分查找」，而是在数组 [1, 2, ……, n] （有序数组）上使用「二分查找」。
"""

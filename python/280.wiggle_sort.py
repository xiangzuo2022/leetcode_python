"""
O(nlogn)
这道题让我们求摆动排序，跟Wiggle Sort II相比起来，这道题的条件宽松很多，只因为多了一个等号。由于等号的存在，当数组中有重复数字存在的情况时，也很容易满足题目的要求。这道题我们先来看一种时间复杂度为O(nlgn)的方法，
思路是先给数组排个序，然后我们只要每次把第三个数和第二个数调换个位置，第五个数和第四个数调换个位置，以此类推直至数组末尾，这样我们就能完成摆动排序了
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        nums.sort()
        while i < n-2:
            nums[i+1], nums[i+2] = nums[i+2], nums[i+1]
            i += 2


"""
这道题还有一种O(n)的解法，根据题目要求的nums[0] <= nums[1] >= nums[2] <= nums[3]....，我们可以总结出如下规律：

当i为奇数时，nums[i] >= nums[i - 1]

当i为偶数时，nums[i] <= nums[i - 1]

那么我们只要对每个数字，根据其奇偶性，跟其对应的条件比较，如果不符合就和前面的数交换位置即可
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1, n):
            if i % 2 == 1 and nums[i] < nums[i-1] or i % 2 == 0 and nums[i] > nums[i-1]:
                nums[i-1], nums[i] = nums[i], nums[i-1]

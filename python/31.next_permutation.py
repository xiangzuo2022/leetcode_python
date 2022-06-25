"""
# 题意： 输出字典序中的下一个排列。比如123生成的全排列是：123，132，213，231，312，321。
# 那么321的next permutation是123。
# 解题思路：输出字典序中的下一个排列。比如123生成的全排列是：123，132，213，231，312，321。
# 那么321的next permutation是123。下面这种算法据说是STL中的经典算法。在当前序列中，从尾端往前寻找两个
# 相邻升序元素，升序元素对中的前一个标记为partition。然后再从尾端寻找另一个大于partition的元素，
# 并与partition指向的元素交换，然后将partition后的元素（不包括partition指向的元素）逆序排列。比如14532，
# 那么升序对为45，partition指向4，由于partition之后除了5没有比4大的数，所以45交换为54，即15432，
# 然后将partition之后的元素逆序排列，即432排列为234，则最后输出的next permutation为15234。确实很巧妙。
"""
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, num):

        lenNum = len(num)
        # find the first number (PartitionNumber) which violates the increase trend
        partitionIndex = -1
        for i in reversed(xrange(lenNum - 1)):
            if num[i] < num[i + 1]:
                partitionIndex = i
                break
        if partitionIndex != -1:
            for i in reversed(xrange(lenNum)):
                if num[i] > num[partitionIndex]:
                    num[i], num[partitionIndex] = num[partitionIndex], num[i]
                    break
        # reverse all numbers behind PartitionIndex
        i = partitionIndex + 1
        j = lenNum - 1
        while i < j:
            num[i], num[j] = num[j], num[i]
            i += 1
            j -= 1



## My own solution

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums); e = None;partition = -1
        for i in reversed(range(1,n)):
            if nums[i] > nums[i-1]:
                partition = i-1
                e = nums[partition]
                break
                
        for i in reversed(range(1,n)):
            if nums[i] > e:                
                nums[i],nums[partition] = nums[partition],nums[i]
                break
        
        nums[partition+1:] = nums[partition+1:][::-1]











        



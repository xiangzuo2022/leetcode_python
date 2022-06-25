class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, A, m, B, n):
        
        lastA, lastB = m-1, n-1     # Travel A and B from right to left
        last2Write = m + n -1       # Write the integers from the rightmost
                                    # position to the leftmost position of A
        
        while lastA != -1 and lastB != -1:
            if A[lastA] >= B[lastB]:
                A[last2Write] = A[lastA]
                lastA -= 1
            else:
                A[last2Write] = B[lastB]
                lastB -= 1
            last2Write -= 1
        
        # If A list has some remaining items to process, they are already in
        # their to-be position. No operation is needed.
        # Otherwise, if B list has some remaining items, copy them to the head
        # of A.
        if lastB != -1:  
        	A[:lastB+1] = B[:lastB+1]

"""
这个题解法非常巧妙， 个人非常喜欢
从前面开始遍历的话， 要插入元素， 这样会影响的后面的元素， 要全部往后移动， 开销太大；
从后面开始遍历， 有空的空间直接存元素， A和B的指针往前移动
"""

"""
九章给的解法：很简但O(nlogn)
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i+m] = nums2[i]
        nums1.sort()



"""
从尾部开始比较的方法:最优解法
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        i = m-1; j = n-1; k = m+n-1
        while i > -1 and j > -1:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1; k-=1
            else:
                nums1[k] = nums2[j]
                j -= 1; k -= 1
        if j > -1: #只用考虑j, i不用考虑
            nums1[:j+1] = nums2[:j+1] 
                
        
       
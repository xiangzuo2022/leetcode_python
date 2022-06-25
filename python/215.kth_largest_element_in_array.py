"""
# O(nlogn)
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
    	return sorted(nums,reverse=True)[k-1]

"""
# http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html
# O(n) 并且不需要额外空间
快速选择排序
执行Partition算法(就是那个快排里将区间内所有数划分为小的一部分和大的一部分的过程)
判断第k大的数是在小的部分还是大的部分
递归,直到区间足够小,返回结果
"""
import random
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2))) # nums2 从k值后算起
        return pivot

"""
注意是第k大不是第k小， 所以从大的算起， 这个地方困惑了我半天
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = nums[0]
        large, small = [], []
        for num in nums:
            if num > pivot:
                large.append(num)
            elif num < pivot:
                small.append(num)
        if k <= len(large):
            return self.findKthLargest(large, k)
        elif k > len(nums) - len(small):
            return self.findKthLargest(small, k - (len(nums) - len(small))) 
        else:
            return pivot


"""
用最大堆
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res
      
"""
大顶堆
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxheap = []
        for num in nums:
            heapq.heappush(maxheap, -num)
        
        for i in range(k):
            res = heapq.heappop(maxheap)
        return -res


More explonations: https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/167837/Python-or-tm

if __name__ == '__main__':
	a = Solution()
	a.findKthLargest([2,1], 1)








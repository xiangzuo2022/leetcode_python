
"""
# Binary search变形题
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
    	#return sorted(nums)[0]
    	def getMin(start,end):
    		if start == end:
    			return nums[end]
    		middle = (start+end)/2
    		if nums[middle] < nums[middle-1]:
    			return nums[middle]
    		elif nums[middle] > num[end]:
    			return getMin(middle+1,end)
    		else:
    			return getMin(start,middle-1)
    	return getMin(0,len(nums)-1)



"""
My own solution: two pointers
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if nums == []: return None
        n = len(nums)
        if n == 1: return nums[0]      
        minValue = nums[0]
        p1 = 0; p2 = 1
        while p2 < n:            
            if nums[p2] >= nums[p1]:
                p2 += 1
            else:
                minValue = nums[p2]
                break
        return minValue

"""
My accepted solution 2
"""
class Solution(object):
    def findMin(self, nums):        
        if not nums:return None
        left = 0
        while left < len(nums)-1:
            right = left + 1
            if nums[left] < nums[right]:
                left += 1
            else:
                return nums[right]
        return nums[0]


"""
adapted from binary search but no recursive
there are three cases. We need to deal with the three cases one by one.
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        left = 0; right = len(nums)-1
        while left <= right:
            if left == right:
                return nums[left]
            mid = (left + right)/2
            if nums[mid] < nums[mid-1]:
                return nums[mid]               
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid -1


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:return None
        if n == 1: return nums[0]
        l = 0; r = n-1;minVal = nums[0]
        while l <= r:
            if l == r:
                return nums[l]
            m = (l+r)/2
            if nums[m] < nums[m-1]:
                return nums[m]
            elif nums[m] < nums[r]:  # cannot compare with left, it's hard to make decision.
                r = m -1
            else:
                l = m + 1


"""
九章的模板解法:
target 不能等于nums[0], 只能nums[-1]
"""
class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        if len(nums) == 0:
            return 0
            
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = (start + end) / 2
            if nums[mid] <= target:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])


"""
Another solution, my own
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return None
        n = len(nums)
        left = 0; right = n-1
        while left+1 < right:
            m = (left+right)/2
            if nums[m] < nums[m-1]:
                return nums[m]
            elif nums[m] < nums[right]:
                right = m
            else:
                left = m
        return min(nums[left],nums[right])















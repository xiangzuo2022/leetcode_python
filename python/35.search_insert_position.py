class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
    	size = len(nums)
    	left, right = 0, size-1
    	while left <= right:
	    	mid = (left + right)/2
	    	if nums[mid] < target:
	    		left = mid + 1
	    	elif nums[mid] > target:
	    		right = mid - 1
	    	else:
	    		return mid
	    return left



# ***************** The Second Time *************
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
    	left = 0; right = len(nums)-1
    	while left <= right:
    		mid = (left + right)/2
    		if nums[mid] < target:
    			left = mid + 1
    		elif nums[mid] > target:
    			right = mid -1
    		else:
    			return mid
    	return left


##### The third time ###################
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0; right = len(nums) - 1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left



"""
九章模板
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:return 0
        n = len(nums)
        left = 0; right = n-1
        while left + 1 < right:
            mid = (left + right)/2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[left] >= target:
            return left
        elif nums[right] >= target:
            return right
        return n

"""
brute force 暴力解法
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        left, right = 0, size-1
        while(left <= right):
            mid = (left + right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
                
        for i in range(size):
            if nums[i] > target:
                return i
        return size
        























	    		


"""
# 解题思路：又是二分查找的变形。因为题目要求的时间复杂度是O(log n)。在二分查找到元素时，需要向前和向后
# 遍历来找到target元素的起点和终点。
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
    	left = 0; right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                res = [0, 0]
                if nums[left] == target: res[0] = left
                if nums[right] == target: res[1] = right
                for i in range(mid, right+1):
                    if nums[i] != target: res[1] = i - 1; break
                for i in range(mid, left-1, -1):
                    if nums[i] != target: res[0] = i + 1; break
                return res
        return [-1, -1]


##### The third time ############
# the running time is O(n)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = [];tmp = []
        if target not in nums:
            return [-1,-1]
        else:
            for i in range(0,len(nums)):
                if nums[i] == target:
                    tmp.append(i)

            if len(tmp) == 1:
                index.append(tmp[0])
                index.append(tmp[0])
            else:
                index.append(tmp[0])
                index.append(tmp[-1])
            return index



"""
My own solution: O(logn)
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        return self.search(0,n-1,target,nums)
        
        
    def search(self,left,right,target,nums):
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        elif len(nums) == 1 and nums[0] != target:
            return [-1,-1]
        
        while left <= right:
            m = (left+right)/2
            if target > nums[m]:
                left = m + 1
            elif target < nums[m]:
                right = m - 1
            else:
                res = [0,0]              
                    
                while m-1 >= left and nums[m-1] == target:
                    m -= 1
                res[0] = m
                while m+1 <= right and nums[m+1] == target:
                    m += 1
                res[1] = m 
                return res
        return [-1,-1]


"""
jiuzhang 模板
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1,-1]
        if not nums:return res
        # find left bound
        left = 0;right = len(nums)-1        
        while left+1 < right:
            m = (left+right)/2
            if nums[m] < target:
                left = m  
            else:
                right = m 
        if nums[left] == target:
            res[0] = left
        elif nums[right] == target:
            res[0] = right
        else:
            return res
        
        left = left; right = len(nums)-1
        while left + 1 < right:
            m = (left+right)/2
            if nums[m] <= target:
                left = m
            else:
                right = m
        if nums[right] == target:
            res[1] = right
        else:
            res[1] = left # 此时left和right相邻， 如果right不等于target，必然是left
        return res           
            
            
                
                    
                    



























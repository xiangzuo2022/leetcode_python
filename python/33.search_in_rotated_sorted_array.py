"""
# ******* The Second Time *******
# 解题思路：二分查找的变种。分别讨论左边单调递增还是右边单调递增.
# 用mid的值和最左和最右的值比较来决定search范围
# As the sequence is rotated, for any mid element, either it is of order with its 
# previous part, or it is of order with its next part. e.g. 561234, middle element 
# 1 has an order with its next part 1234.
# 5678123, middle element 8 has an order with its previous part 5678.
# Normal binary search just compare the middle element with the target, here we need 
# more than that.
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
    	left = 0; right = len(nums) - 1
    	while left <= right:
    		mid = (left + right)/2
    		if nums[mid] == target:
    			return mid
    		if nums[mid] >= nums[left]:
    			if target >= nums[left] and target < nums[mid]:
    				right = mid - 1
    			else:
    				left = mid + 1
    		else:
    			if target > nums[mid] and target <= nums[right]:
    				left = mid + 1
    			else:
    				right = mid -1
    	return -1




"""
 九章模板: mid 和start比较来决定 > m 的值实在左边还是右边， 两种情况是相反的
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:return -1
        start = 0; end = len(nums)-1
        while start + 1 < end:
            m = (start + end)/2
            if nums[m]==target:return m
            if nums[start] < nums[m]:
                if nums[start] <= target and target <= nums[m]:
                    end = m
                else:
                    start = m
            else:
                if nums[m] <= target and target <= nums[end]:
                    start = m
                else:
                    end = m
        if nums[start] ==  target:
            return start
        if nums[end] == target:
            return end
        return -1


"""
official solution
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-leetcode-solut/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# https://www.youtube.com/watch?v=U8XENwh8Oy8&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=8
# binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            # left sorted portion
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1          
            else: # right sorted portion
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
        













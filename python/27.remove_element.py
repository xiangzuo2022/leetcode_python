"""
此方法很巧妙
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
    	
    	tail = 0
    	for e in nums:
    		if e != val:
    			nums[tail] = e    			
    			tail += 1
    	return tail


"""
Solution 2, 速度慢， 因为要删除元素
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
        


"""
有种错误的解法：len(nums)是动态变化的， 会造成数组越界异常
"""
def removeElement(self, nums, val):
        for i in range(len(nums)):
            if val == nums[i]:
                del nums[i]
        return len(nums)


"""
two pointers
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        n = len(nums)
        if n == 0:
            return len(nums)
        end = n-1
        start = 0
        while start <= end:
            if nums[start] == val:
                nums[start] = nums[end]
                end -= 1
            else:
                start += 1
        return len(nums[:end+1])

"""
双指针法
双指针法（快慢指针法）： 通过一个快指针和慢指针在一个for循环下完成两个for循环的工作。
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,n = 0,len(nums)
        for j in range(n):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == '__main__':
	a = Solution()
	nums = [4,5,5]
	print a.removeElement(nums,5)

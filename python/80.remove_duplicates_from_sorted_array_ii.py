"""以下做法用了额外数组和字典
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
    	res = []
    	d = {}
    	if not nums:
    		return 0
    	for item in nums:
    		if item not in d:
    			d[item] = 1
    		else:
    			d[item] += 1

    	for key in d:
    		if d[key] == 1:
    			res.append(key)
    		elif d[key] >= 2:
    			res.append(key)
    			res.append(key)
    			
    	print res
    	return len(res)

"""
# solution from online: 
# 解题思路：一种巧妙的解法。使用两个指针prev和curr，判断A[curr]是否和A[prev]、A[prev-1]相等，
# 如果相等curr指针继续向后遍历，直到不相等时，将curr指针指向的值赋值给A[prev+1]，这样多余的数就都被
# 交换到后面去了(我认为时抹掉了)。最后prev+1值就是数组的长度。
"""



def removeDuplicates(self, nums):
    if len(nums) <= 2:
        return len(nums)
    prev = 1; curr = 2
    while curr < len(nums):
        if nums[curr] == nums[prev] and nums[curr] == nums[prev-1]:
            curr += 1
        else:
            prev += 1
            nums[prev] = nums[curr]
            curr += 1
    return prev + 1  # prev begins from 0 so the length is (prev+1)


"""
The third time: 我自己写的， 思路是对的， 但是代码不够简洁
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if nums == []: return 0
        if len(nums) == 1: return 1
        i= 0; j = 1
        while i < len(nums)-1 and j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
            #$tmp = nums[i+1]
                nums[i+1] = nums[j]
                nums[j] = nums[i+1]
                i += 1
                j += 1
        return i + 1

"""
改进代码， 思想不变
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums): 
        if len(nums) <= 1: return len(nums)
        i= 0; j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                #tmp = nums[i+1]
                nums[i+1] = nums[j]
                nums[j] = nums[i+1]
                i += 1
                j += 1
        return i + 1


"""
一下解法是错误的：only比较相邻的两个元素然后置换的尾部无法删除所有相同element
[1112334]-->[14132311]
"""
n = len(nums)
        if n <= 1: return n
        prev = 0; cur = 1;tail = n-1
        while cur < n and cur < tail:
            if nums[prev] == nums[cur]:
                nums[cur],nums[tail] = nums[tail],nums[cur]
                tail -= 1
            else:
                prev += 1
                cur += 1
        nums[:] = nums[:cur-1]
        return prev+1


"""
only compare j-2 and i
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        j = 2
        for i in range(2, n):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j += 1

        return j

        
    

               


if __name__ == '__main__':
	a = Solution()
	print a.removeDuplicates([1,1,1,2])

	# don't know what's wrong with my codes
#  刷了几道了Array的题，感觉有一些相似的技巧，就是只遍历一次，不满足条件就交换元素位置。
# 不占用额外的空间。




import math

class Solution:
    # @param {integer[]} nums
    # @return {integer}

    # 解法1
    def majorityElement(self, nums):
		freq = len(nums)/2		
		major_elem = []
		d = {}
		for item in nums:
			d.setdefault(item,[]).append(1)
		for key in d:
			if len(d[key]) >= freq:
				return key


    # 解法2
    def majorityElement(self, num):
	   	num.sort()	   
	   	return num[int(len(num)/2)]



#******** The Second Time **********
"""
解法不是最优O(nlogn)
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
    	nums.sort()
    	return nums[len(nums)/2]

    	

"""The Third Time
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        if nums == []:return None
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        for key in d:
            if d[key] > len(nums)/2:
                return key
        return None



"""
jiuzhang O(n) solution:出来打架， 一个对一个， 最后剩的就是majority majority element
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        candidate = None;count = 0
        for i in range(0,len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            elif candidate == nums[i]:
                count += 1
            else:
                count -= 1
        return candidate

"""
Boyer-Moore 投票算法
如果我们把众数记为 +1+1，把其他数记为 −1−1，将它们全部加起来，显然和大于 0，从结果本身我们可以看出众数比其他数多。
算法
Boyer-Moore 算法的本质和方法四中的分治十分类似。我们首先给出 Boyer-Moore 算法的详细步骤：
我们维护一个候选众数 candidate 和它出现的次数 count。初始时 candidate 可以为任意值，count 为 0；
我们遍历数组 nums 中的所有元素，对于每个元素 x，在判断 x 之前，如果 count 的值为 0，我们先将 x 的值赋予 candidate，随后我们判断 x：
如果 x 与 candidate 相等，那么计数器 count 的值增加 1；
如果 x 与 candidate 不等，那么计数器 count 的值减少 1。
在遍历完成后，candidate 即为整个数组的众数。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/majority-element/solution/duo-shu-yuan-su-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate




class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        return candidate




    			


if __name__ == '__main__':
	b = Solution()
	array = [8,8,7,7,7,8]

	print b.majorityElement(array)
	print b.majorityElement2(array)




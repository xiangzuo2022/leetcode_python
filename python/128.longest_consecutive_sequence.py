"""
# 我的思想方法是对的， 但是不能完整地写出代码
# 用dictionary, get item的平均时间复杂度为O(1), 可以把key设为list中的数, value用于标记是
# 否访问过。遍历所有的key, 不断找寻其+1和-1得到的值是否在dictionary中, 记下最长的连续序列长度。
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
    	d = {x:False for x in nums}
    	count = -1
    	for i in d:
    		if d[i] == False:
    			curr = i + 1; lenright = 0
    			while curr in d:
    				lenright += 1; d[curr] = True; curr += 1
    			curr = i -1; lenleft = 0
    			while curr in d:
    				lenleft += 1; d[curr] = True; curr -= 1
    			count = max(count,lenleft+1+lenright)
    	return count


"""
jiuzhang solution: use hash 
用每个元素进出数据结构的次数来判断时间复杂度
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict(); n = len(nums); longest = 0
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = 1
        
        for i in range(n):
            down = nums[i]-1
            while down in d:
                del d[down]  #删除对应的元素就不用重复计算
                down -= 1
            up = nums[i]+1
            while up in d:
                del d[up]
                up += 1
            longest = max(longest,up-down-1)
        return longest


"""
official solution
"""
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    		
"""
采用集合的写法
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        for num in nums:
        	# 判断是否是第一个数字
            if num - 1 not in nums:
                tmp = 1
                while num + 1 in nums:
                    num += 1
                    tmp += 1
                res = max(res, tmp)
        return res

"""
use hashtable的实现
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = {}
        res = 0
        for num in nums:
            if num not in lookup:
                # 判断左右是否可以连起来
                left = lookup[num - 1] if num - 1 in lookup else 0
                right = lookup[num + 1] if num + 1 in lookup else 0
                # 记录长度
                lookup[num] = left + right + 1
                # 把头尾都设置为最长长度
                lookup[num - left] = left + right + 1
                lookup[num + right] = left + right + 1
                res = max(res, left + right + 1)
        return res
    

# https://www.youtube.com/watch?v=P6RZZMu_maU
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


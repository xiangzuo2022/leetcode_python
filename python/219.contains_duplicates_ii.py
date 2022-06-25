
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
    	d = {}
    	for position, value in enumerate(nums):
    		d.setdefault(value,[]).append(position)
    	for key in d:    	
    		if len(d[key]) > 1:    			
    			for i in range(0,len(d[key])-1):
    				if abs(d[key][i] - d[key][i+1]) <= k:    			
    					return True
    	return False


    # 网上的解法, 代码非常简洁, 字典是比较的同时也赋值
    def containsNearbyDuplicate(self, nums, k):
        d = dict()
        for i in range(len(nums)):
            index = d.get(nums[i])
            if index >= 0 and abs(i - index) <= k:
                return True
            d[nums[i]] = i 
        return False

"""
Another solution uses dictionary and enumerate
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        n = len(nums)
        for index, value in enumerate(nums):
            if value in d and index - d[value] <= k:
                return True
            d[value] = index
        return False

if __name__ == '__main__':
	a = Solution()
	print a.containsNearbyDuplicate([1,0,1,1],1)


    # 解题思路：用一个字典记录相同value值的位置， 然后进行判断
    # 此题需要看一下网上的解法， 这只是我个人的解法


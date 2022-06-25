class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
    	length = len(nums)
    	if length == 0:
    		return []
    	if length == 1:
    		return [nums]
    	num.sort()   # after sorting, it's convinent to find duplicates
    	res = []
    	previsouNum = None
    	for i in range(length):
    		if nums[i] == previsouNum:
    			continue
    		previsouNum = nums[i]
    		for j in self.permuteUnique(nums[:i]+nums[i+1:]):
    			res.append([nums[i]]+j)
    	return res


# ******** The Second Time *********
# 以下方法， TLE
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        def dfs(depth,value):
            if depth == len(nums):
                if value not in ans:
                    ans.append(value)
            for i in range(len(nums)):
                dfs(depth+1,value+[nums[i]])
        ans = []
        dfs(0,[])
        return ans

"""
# 解题思路：这道题也是穷举全排列，只是集合中可能有重复的元素。分两步：1，对集合进行排序。2，进行剪枝，
# 如果元素重复，直接跳过这一元素，决策树的这一枝被剪掉。
# 和Permutation那道题目差不多，也是递归，不过要去重。先排序，再利用prevNum变量区分是否重复。
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        n = len(nums)
        if n == 0: return []
        if n == 1: return [nums]
        nums.sort()
        res = []
        preNum = None  # record the previous element

        for i in range(n):
            if nums[i] == preNum:
                continue
            else:
                preNum = nums[i]
            for j in self.permuteUnique(nums[:i]+nums[i+1:]): # 经常用的技巧
                res.append([nums[i]] + j)
        return res



"""
The forth time: if you use if ([nums[i]]+j) not in ans:
                    ans.append([nums[i]]+j)
will have time out problem. Because the if statment is time consuming. 
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums);ans = []
        if n == 0:return []
        if n == 1: return [nums]
        nums.sort()
        preNum = None

        for i in range(n):
            if nums[i] == preNum:
                continue
            else:
                preNum = nums[i]
            for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                ans.append([nums[i]]+j)
        return ans
            
"""
与46一样的解法
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, value):
            if len(nums) == 0 and value not in ans:
                ans.append(value)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], value+[nums[i]])
            
        ans = []
        dfs(nums, [])
        return ans


"""
new backtrack template: remove duplicates and used array 
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        nums = sorted(nums)
        used = [0] * len(nums)
        def backtrack(nums):
            if len(path) == len(nums):                
                ans.append(path[:])   
                return
            for i in range(0, len(nums)):
                if not used[i]:
                    if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                        continue
                    used[i] = 1
                    path.append(nums[i])
                    backtrack(nums)
                    path.pop()
                    used[i] = 0
        backtrack(nums)
        return ans

























class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
    	if not nums:
    		return []
    	if len(nums) == 1:
    		return [nums]

    	res = []
    	for i in range(len(nums)):
    		print 'i:',i,nums[:i]+nums[i+1:]

           	for j in self.permute(nums[:i] + nums[i+1:]): # except nums[i]
           		
           		res.append([nums[i]] + j)
        return res

if __name__ == '__main__':
	a = Solution()
	print a.permute([1,2,3])


"""
# ******* The Second Time *********
# 解题思路：穷举一个集合的全排列。这个就是python递归巧妙的使用了。
# 把一个数组拆成两部分的思想经常使用
# 此解法非常巧妙,仔细想想很有意思
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
      if len(nums) == 0: return []
      if len(nums) == 1: return [nums] #这个条件非常重要是递归产生结果的关键一步
      res = []
      for i in range(len(nums)):
        for j in self.permute(nums[:i] + nums[i+1:]):  # 没有nums[i]；巧妙在此处
          res.append([nums[i]] + j)
      return res

"""
discuss里看到的用DFS实现的方法
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums,value): 
            if len(nums) == 0:  # 这个条件一开始写错了          
                ans.append(value)                
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],value+[nums[i]])
        ans = []
        dfs(nums,[])
        return ans



"""
use the template of backtracking
"""    
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        def backtrack(nums):
            if len(path) == len(nums):
                return ans.append(path[:])                
            for i in range(0, len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(nums)
                path.pop()
        backtrack(nums)
        return ans

























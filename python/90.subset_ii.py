# 解题思路：和上一道题一样，求一个集合的所有子集。和上一道题不一样的一点是集合可能有重复元素。
# 这道题同样使用dfs来解题，只是需要在dfs函数里加一个剪枝的条件，排除掉同样的子集。
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
    	def dfs(depth,start,value):
    		if value not in ans:
    			ans.append(value)
    		if depth == len(nums):
    			return
    		for i in range(start,len(nums)):
    			dfs(depth+1,i+1,value+[nums[i]])
		ans = []
		nums.sort()
		dfs(0,0,[])
		return ans


# ********** The Second Time **********
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        def dfs(depth,start,value):
            if value not in ans:
                ans.append(value)
            if depth == len(nums):
                return 
            for i in range(start,len(nums)):
                dfs(depth+1, i+1,value+[nums[i]])
        nums.sort()
        ans = []
        dfs(0,0,[])
        return ans

# ************************ The Third Time *******************
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(depth,start,value):
            if value not ans:
                ans.append(value)
            if depth == len(nums):
                return
            for i in range(start,len(nums)):
                dfs(depth+1,i+1,value+[nums[i]])


        nums.sort()
        ans = []
        dfs(0,0,ans)
        return ans
      
      
      """
      remove duplicates: sort and nums[i] != nums[i-1]
      """
    class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        nums = sorted(nums)
        def backtrack(nums, startIndex):
            #if path not in ans:
            ans.append(path[:])
            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()
        backtrack(nums, 0)
        return ans























        

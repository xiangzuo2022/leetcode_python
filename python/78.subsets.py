class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []
        def backtrack(nums, startIndex):
         
            ans.append(path[:])
            
           
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()
        backtrack(nums, 0)
        return ans
    
# https://www.youtube.com/watch?v=REOH22Xwdkk
# backtracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):  # i is the index
            if i >= len(nums):
                res.append(subset.copy())
                return 
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # decision not to include nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res
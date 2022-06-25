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
"""
cannot use sorting method to remove duplicates because it requires an increasing array. 
So here repeat[] is used for remove duplicates
"""

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        path = []
       
        def backtrack(nums, startIndex):
            repeat = []
            if len(path) >= 2 :
                ans.append(path[:])
                
            for i in range(startIndex, len(nums)): 
                if nums[i] in repeat:
                    continue
                if len(path) >= 1 and nums[i] < path[-1]:
                    continue
                repeat.append(nums[i])
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()
        backtrack(nums, 0)
        return ans
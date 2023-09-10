class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for index, val in enumerate(nums):
            if (target - val) in d:
                return [d[target-val], index]
            d[val] = index


dictionary stores value and the value of d is the index

"""
my own solution with hashtable. The logic is more clear
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
    
        for i, val in enumerate(nums):
            if target - val not in d:
                d[val] = i
            else:
                return [d[target-val], i]
              
"""
更容易懂的hashmap解法
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
            

# https://www.youtube.com/watch?v=KLlXCFG5TnA
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        
        for index, val in enumerate(nums):
            diff = target - val
            if diff not in d:
                d[val] = index
            else:
                return [d[diff], index]
        return []
                

# https://www.youtube.com/watch?v=WnPLSRLSANE
# solution1: sum1 - sum2 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
    
# solution 2: XOR
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        for i in range(len(nums)+1):
            ans ^= i
        return ans
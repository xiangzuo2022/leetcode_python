"""
similar solution as 3sums but needs one more for loop
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        if not nums: return ans
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            if i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-1):
                if j!=i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1; right = n-1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        ans.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left +=1; right -= 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
        return ans



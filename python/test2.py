class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        ans = []; n = len(nums)
        #if n < 3:return ans
        for i in range(n-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            left = i + 1; right = n-1
            while left < right:
                sums = nums[left] + nums[right] + nums[i]
                
                if sums == 0:
                    ans.append(([nums[i],nums[left],nums[right]]))
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1;right -= 1

                elif sums < 0:
                    left += 1
                else:
                    right -= 1
               
        return ans



if __name__ == '__main__':
    a = Solution()
    print a.threeSum([-2,0,1,1,2])








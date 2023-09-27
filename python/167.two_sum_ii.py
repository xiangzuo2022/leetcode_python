class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        n = len(numbers)
        left, right = 0,n-1
        while left <= right:
            
            if (numbers[left] + numbers[right]) == target:
                res.append(left+1)
                res.append(right+1)
                break
            elif (numbers[left] + numbers[right]) > target:
                right -= 1
            else:
                left += 1
        return res
    

# https://www.youtube.com/watch?v=cQ1Oz4ckceM
# two pointers O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
        return []
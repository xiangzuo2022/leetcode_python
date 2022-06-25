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
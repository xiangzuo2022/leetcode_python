#chatgpt
def splitArray(nums, k):
    def is_valid(mid):
        count = 1
        current_sum = 0
        for num in nums:
            if current_sum + num > mid:
                count += 1
                current_sum = num
            else:
                current_sum += num
        return count <= k

    left = max(nums)
    right = sum(nums)
    
    while left < right:
        mid = (left + right) // 2
        if is_valid(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Example usage:
nums = [7, 2, 5, 10, 8]
k = 2
result = splitArray(nums, k)
print(result)  # Output should be 18

# A good youtube video: https://www.youtube.com/watch?v=YUF3_eBdzsk&t=51s


class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canSplit(largest):
            subarray = 1
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    curSum = n 

            return subarray  <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + (r - l)//2
            if canSplit(mid):
                res = mid
                r = mid -1
            else:
                l = mid + 1
        return res

"""
some of the calculations just have no reason. Remember them !
"""

def missingElement(nums, k):
    # Return how many numbers are missing until nums[idx]
    missing = lambda idx: nums[idx] - nums[0] - idx
            
    n = len(nums)
    # If kth missing number is larger than 
    # the last element of the array
    if k > missing(n - 1):
        return nums[-1] + k - missing(n - 1) 

    idx = 1
    # find idx such that 
    # missing(idx - 1) < k <= missing(idx)
    while missing(idx) < k:
        idx += 1

    # kth missing number is greater than nums[idx - 1]
    # and less than nums[idx]
    return nums[idx - 1] + k - missing(idx - 1)

# missingElement([4, 7, 9, 10], 3)

def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(1, len(nums)):
            k -= (nums[i]-nums[i-1]-1)   # How many missing numbers we still need to find out
            if k <= 0:   # It must exist somewhere between nums[i]-nums[i-1]
                return nums[i] + k - 1  # Calculate this using example 1 
        return nums[-1]+k # k is larger than the last element in nums
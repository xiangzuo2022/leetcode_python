"""
此题技巧在于preSum + hashmap
sum of subarray(i, j) = prefixSum[j] - prefixSum[i-1]
where i < j, prefixSum[j] - prefixSum[i] == k
https://www.youtube.com/watch?v=aYfwus5T3Bs
"""

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        d = {0: -1}
        if not nums:
            return 0
        sums = 0
        maxlen = 0
        for i in range(n):
            sums += nums[i]
            if sums-k in d:
                maxlen = max(maxlen, i - d[sums-k])
            if sums not in d:
                d[sums] = i

        return maxlen

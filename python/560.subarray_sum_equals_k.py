"""
This solution gets time out for python
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        sum = [0] * (n+1)
        for i in range(1, n+1):
            sum[i] = sum[i-1] + nums[i-1]
        
        for i in range(n):
            for j in range(i+1, n+1):
                if(sum[j] - sum[i] == k):
                    count += 1
        return count
      
"""
用一个 HashMap 来建立连续子数组之和跟其出现次数之间的映射，初始化要加入 {0,1} 这对映射，这是为啥呢，因为解题思路是遍历数组中的数字，
用 sum 来记录到当前位置的累加和，建立 HashMap 的目的是为了可以快速的查找 sum-k 是否存在，即是否有连续子数组的和为 sum-k，如果存在的话，
那么和为k的子数组一定也存在，这样当 sum 刚好为k的时候，那么数组从起始到当前位置的这段子数组的和就是k，满足题意，如果 HashMap 
中事先没有 m[0] 项的话，这个符合题意的结果就无法累加到结果 res 中，这就是初始化的用途。
O(n)
"""    

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        d = {0:1}       
        s = 0
        for num in nums:
            s += num
            res += d.get(s-k, 0)
            d[s] = d.get(s, 0) + 1
        return res
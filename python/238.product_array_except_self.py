"""
属于要记住解法的题
我们以一个4个元素的数组为例，nums=[a1,a2,a3,a4]，要想在O(n)的时间内输出结果，比较好的解决方法是提前构造好两个数组：
[1, a1, a1*a2, a1*a2*a3]
[a2*a3*a4, a3*a4, a4, 1]
然后两个数组一一对应相乘，即可得到最终结果 [a2*a3*a4, a1*a3*a4, a1*a2*a4, a1*a2*a3]。
不过，上述方法的空间复杂度为O(n)，可以进一步优化成常数空间，即用一个整数代替第二个数组。
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 1
        n = len(nums)
        res = [1]*n

        for i in range(n-1):
            left *= nums[i]
            res[i+1] *= left

        right = 1
        for i in range(n-1, 0, -1):
            right *= nums[i]
            res[i-1] *= right
        return res
      
      
"""
Algorithm:
Initialize two empty arrays, L and R where for a given index i, L[i] would contain the product of all the numbers to the left of i 
and R[i] would contain the product of all the numbers to the right of i.
We would need two different loops to fill in values for the two arrays. For the array L, L[0]L[0] would be 1 since there are no elements 
to the left of the first element. For the rest of the elements, we simply use L[i]=L[i−1]∗nums[i−1]L[i]=L[i−1]∗nums[i−1]. 
Remember that L[i] represents product of all the elements to the left of element at index i.
For the other array, we do the same thing but in reverse i.e. we start with the initial value of 1 in R[length−1]R[length−1] where lengthlength 
is the number of elements in the array, and keep updating R[i] in reverse. Essentially, R[i]=R[i+1]∗nums[i+1]R[i]=R[i+1]∗nums[i+1]. 
Remember that R[i] represents product of all the elements to the right of element at index i.
Once we have the two arrays set up properly, we simply iterate over the input array one element at a time, and for each element at index i, 
we find the product except self as L[i]∗R[i]L[i]∗R[i].
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        ans = [0] * n
        
        l, r = [0] * n, [0] * n
        l[0] = 1
        
        
        for i in range(1, n):
            l[i] = l[i-1] * nums[i-1]
            
        r[n-1] = 1
        for i in reversed(range(n-1)): # here needs to be reversed because we need to first have r[i+1] value then calculater r[i]
            r[i] = r[i+1] * nums[i+1]
        
        for i in range(n):
            ans[i] = l[i] * r[i]
        return ans
  
  """
  leetcode's solution is more clear: the same idea as above but ultilizing ans[] to store left product values and r 
  stores right product values.
  """     
  class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """        
        n = len(nums)
        ans = [1] * n      
        
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
            
        r = 1
        for i in reversed(range(n)):
            ans[i] = ans[i] * r
            r = r * nums[i]
        return ans
    

# https://www.youtube.com/watch?v=bNvIQI2wAjk&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=4
# prefix * postfiex
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res   
        
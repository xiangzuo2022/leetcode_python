"""
https://www.youtube.com/watch?v=TZyBPy7iOAw
two passes
 主要思想是单调栈
"""
class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 0: return 0
        if n == 1: return arr[0]
        ans = 0
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if not stack:
                right[i] = n
            else:
                right[i] = stack[-1]
            stack.append(i)
        
        for i in range(n):
            ans += (i - left[i]) * (right[i] - i) * arr[i]
            
        return ans % (10**9 + 7) 
      
"""
one pass ?? don't understand
"""
class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        A = [float('-inf')] + A + [float('-inf')]
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] > a:
                cur = stack.pop()
                ans += A[cur] * (i-cur) * (cur-stack[-1])
            stack.append(i)
        return ans % (10**9 + 7)

作者：smoon1989
链接：https://leetcode-cn.com/problems/sum-of-subarray-minimums/solution/dan-diao-zhan-python3-by-smoon1989/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。   

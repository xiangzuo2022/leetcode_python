"""
Online explanation: http://www.cnblogs.com/grandyang/p/4952464.html
not easy to do by myself, need more practice.
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = nums
        n = len(nums)
        for i in range(1, n):
            self.dp[i] += self.dp[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j] - (self.dp[i - 1] if i > 0 else 0)

index begins from 0 so dp[i-1]

方法三：缓存
上面的方法需要很大的空间，我们可以优化它吗？
假设我们预先计算了从数字 0 到 k 的累积和。我们可以用这个信息得出 sum(i，j) 吗？
让我们将 sum[k]sum[k] 定义为 nums[0cdots k-1]nums[0⋯k−1] 的累积和（包括这两个值）：
sum[k] = \left\{ \begin{array}{rl} \sum_{i=0}^{k-1}nums[i] & , k > 0 \\ 0 &, k = 0 \end{array} \right.
sum[k]={ 
∑ 
i=0
k−1
​	
 nums[i]
0
​	
  
,k>0
,k=0
​	
 

现在，我们可以计算 sumrange 如下：
sumrange（i，j）=sum[j+1]-sum[i]
sumrange（i，j）=sum[j+1]−sum[i]

作者：LeetCode
链接：https://leetcode-cn.com/problems/range-sum-query-immutable/solution/qu-yu-he-jian-suo-shu-zu-bu-ke-bian-by-leetcode/


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
"""
Solution 1, Two Loops Solution
Time O(n^2)
Space O(1)
"""
def subArrayRanges(self, nums):
  res = 0
  n = len(nums)
  for i in range(n):
    l, r = nums[i], nums[i]
    for j in range(i, n):
      l = min(l, nums[j])
      r = max(r, nums[j])
      res += r - l
  return res

"""
Solution 2, O(n) Stack Solution
不了解单调栈的同学可以看一下 496. 下一个更大元素 I。
我们可以考虑每个元素作为最大值出现在了多少子数组中，以及作为最小值出现在了多少子数组中。

以最大值为例。我们可以求出 \textit{nums}[i]nums[i] 左侧严格大于它的最近元素位置 \textit{left}[i]left[i]，以及右侧大于等于它的最近元素位置 \textit{right}[i]right[i]。注意 \textit{nums}nums 中可能有重复元素，所以这里右侧取大于等于，这样可以避免在有重复元素的情况下，重复统计相同的子数组。

作者：endlesscheng
链接：https://leetcode-cn.com/problems/sum-of-subarray-ranges/solution/cong-on2-dao-ondan-diao-zhan-ji-suan-mei-o1op/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
 def subArrayRanges(self, A0):
        res = 0
        inf = float('inf')
        A = [-inf] + A0 + [-inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res -= A[j] * (i - j) * (j - k)
            s.append(i)
            
        A = [inf] + A0 + [inf]
        s = []
        for i, x in enumerate(A):
            while s and A[s[-1]] < x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res
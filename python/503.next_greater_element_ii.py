"""
使用取模运算 可以把下标 ii 映射到数组 numsnums 长度的 0−N0−N 内。
时间复杂度：O(N)O(N)，遍历了两次数组；
空间复杂度：O(N)O(N)，使用了额外空间「单调栈」，最坏情况下，栈内会保存数组的所有元素。
"""
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        res = [-1] * N
        stack = []
        for i in range(N * 2):
            while stack and nums[stack[-1]] < nums[i % N]:
                res[stack.pop()] = nums[i % N]
            stack.append(i % N)
        return res

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/next-greater-element-ii/solution/dong-hua-jiang-jie-dan-diao-zhan-by-fuxu-4z2g/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
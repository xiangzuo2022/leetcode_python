"""
O(n)非常巧妙的greedy解法,利用两个辅助pointer inc, dec分别保存当前状态为递增/递减的子序列的最大长度。
"""
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 1
        q = 1
        n = len(nums)
        for i in range(1, n):
            if (nums[i] > nums[i - 1]):
                p = q + 1
            elif (nums[i] < nums[i - 1]):
                q = p + 1

        return min(n, max(p, q))

"""
局部最优：删除单调坡度上的节点（不包括单调坡度两端的节点），那么这个坡度就可以有两个局部峰值。

整体最优：整个序列有最多的局部峰值，从而达到最长摆动序列。
此题做过就会
"""
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preDiff, curDiff, ans = 0, 0, 1
        for i in range(len(nums)-1):
            curDiff = nums[i+1] - nums[i]
            if curDiff * preDiff <= 0 and curDiff != 0:
                ans += 1
                preDiff = curDiff
        return ans
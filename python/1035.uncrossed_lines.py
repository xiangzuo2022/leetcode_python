"""
the same as 1143此题分析后发现就是求最大公共子串
"""
class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m, n  = len(nums1)+1, len(nums2)+1
        dp = [[0] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
        
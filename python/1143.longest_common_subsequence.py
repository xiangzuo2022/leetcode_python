class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1)+1, len(text2)+1
        dp = [[0 for _ in range(len1)] for _ in range(len2)] # 先对dp数组做初始化操作
        for i in range(1, len2):
            for j in range(1, len1): # 开始列出状态转移方程
                if text1[j-1] == text2[i-1]:
                    dp[i][j] = dp[i-1][j-1]+1 
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
      
      
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n1 = len(text1) + 1
        n2 = len(text2) + 1
        dp = [[0 for _ in range(n2)] for i in range(n1)]
        for i in range(1, n1):
            for j in range(1, n2):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
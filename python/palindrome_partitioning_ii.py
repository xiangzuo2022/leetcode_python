class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        dp = [0 for i in range(len(s)+1)]
        p = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)+1):
            dp[i] = len(s) - i
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (((j - i) < 2) or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(1+dp[j+1], dp[i])
        return dp[0]-1
        

"""
jiuzhang idea, my own Solution
"""
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [(i-1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(i):
                temp = s[j:i]
                if temp[:] == temp[::-1]:
                    dp[i] = min(dp[i],dp[j] + 1)
        return dp[n]  #字符串考虑多开一个所以返回是n 不是 n-1
    	
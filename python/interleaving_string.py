# 我开始没想到是DP
# 动态规划, dp[i][j] = m的含义是s1的前i个字母和s2的前j个字母可以成功组成s3的前m个字母, 
# 当dp[len_s1][len_s2]==len_s3时返回True。

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
    	len1 = len(s1); len2 = len(s2); len3 = len(s3)
    	if len1 + len2 != len3: return False
    	dp = [[0 for i in range(len2+1)] for j in range(len1+1)] # 先len2后len1
    	for i in range(len1+1):
    		for j in range(len2+1):
    			if i > 0 and dp[i-1][j] == i-1+j and s1[i-1] == s3[i-1+j]: # 字符串个数和内容都相同
    				dp[i][j] = i + j
    			if j > 0 and dp[i][j-1] == i + j -1 and s2[j-1] == s3[i+j-1]:
    				dp[i][j] = i + j
    	return dp[len1][len2] == len3


"""
jiuzhang Solution：视频讲解很好
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1); n = len(s2)
        if (m+n) != len(s3):return False
        f = [[False for i in range(n+1)] for i in range(m+1)]
        f[0][0] = True
        for i in range(m+1):
            if (s1[:i] == s3[:i]):
                f[i][0] = True
                
        for j in range(n+1):
            if s2[:j] == s3[:j]:
                f[0][j] = True
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (s1[i-1] == s3[i+j-1] and f[i-1][j]) or (s2[j-1] == s3[i+j-1] and f[i][j-1]) :
                    f[i][j] = True
        return f[m][n]
        






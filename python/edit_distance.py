class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
    	m = len(word1) + 1; n = len(word2) + 1
    	dp = [[o for i in range[n]] for j in range[m]]
    	for i in range(n):
    		dp[0][i] = i 
    	for i in range(m):
    		dp[i][0] = i 
    	for i in range(1,m):
    		for j in range(1,n):
    			dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1, dp[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1))
    	return dp[m-1][n-1]


 # http://www.cnblogs.com/zuoyuan/p/3773134.html
 # also need to find other solutions


# ****** The Second Time ********
# 动态规划。dp[i][j]表示word1前i个字母变成word2前j个字母的步数(edit distance)。如果word1的第i个
# 字母等于word2的第j个字母, 则dp[i][j] = dp[i-1][j-1]。如果不等, 则有三种情况:
# 1) 把word1的前i-1个字母变成word2的前j-1个字母, 再把word1的第i个字母换成word2的第j个字母, 即dp[i-1][j-1] + 1
# 2) 把word1的前i个字母变成word2的前j-1个字母, 再加上word2的第j个字母, 即dp[i][j-1] + 1
# 3) 删掉word1的第i个字母, 把word1的前i-1个字母变成word2的前j个字母, 即1 + dp[i-1][j]
# 三种情况的最小值就是dp[i][j]。
# 初始情况: 而dp[i][0]显然等于i，因为只需要做i次删除操作就可以了。同理dp[0][i]也是如此，等于i，因为只需做i次插入操作就可以了。

 class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        len1 = len(word1); len2 = len(word2)
        dp = [[0 for i in range(len2+1)] for j in range(len1+1)]
        for i in range(len1+1):
            dp[i][0] = i 
        for j in range(len2+1):
            dp[0][j] = j
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1]+1)
        return dp[len1][len2]

# 这道dp不太好想



"""
 双序列DP，就是Longest Common Subsequence的变形
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1); n = len(word2)
        f = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            f[i][0] = i
        for j in range(n+1):
            f[0][j] = j
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i-1][j],f[i][j-1],f[i-1][j-1]) + 1
        return f[m][n]


# f[i-1][j-1] --- replace
# f[i][j-1] --- insert
# f[i-1][j] --- delete














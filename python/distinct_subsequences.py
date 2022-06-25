"""
九章视频讲得很好
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
    	dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
    	for j in range(len(s)+1):
    		dp[j][0] = 1
    	for i in range(1,len(s)+1):
    		for j in range(1,len(t)+1):
    			if s[i-1] == t[j-1]:
    				dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    			else:
    				dp[i][j] = dp[i-1][j]
    	return dp[len(s)][len(t)]

# [解题方法] 此题需要使用大数运算。使用一点 DP 即可。关键是如何得到递推关系，可以这样想，设母串的长度为 j，
# 子串的长度为 i，我们要求的就是长度为 i 的字串在长度为 j 的母串中出现的次数，设为 t[i][j]，若母串的最后一
# 个字符与子串的最后一个字符不同，则长度为 i 的子串在长度为 j 的母串中出现的次数就是母串的前 j - 1 个字符中
# 子串出现的次数，即 t[i][j] = t[i][j - 1]，若母串的最后一个字符与子串的最后一个字符相同，那么除了前 j - 
# 1 个字符出现字串的次数外，还要加上子串的前 i - 1 个字符在母串的前 j - 1 个字符中出现的次数，即 t[i][j] = 
# t[i][j - 1] + t[i - 1][j - 1]。  
# http://fisherlei.blogspot.com/2012/12/leetcode-distinct-subsequences_19.html

# ******** The Second Time *******
# 题的意思是：S的所有子串中，有多少子串是T;初始化状态如何确定呢：
# dp[0][j]=0；因为：S是空串，则无论如何都不能包含非空的子串。这个初始状态在初始化矩阵dp的时候就顺带
# 包括了;  dp[i][0]=1；因为：S[0...i-1]只有一个子串是空串。初始化的时候注意空串是任意字符串的子串.
# 这个题目思路不是很好想
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1

        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(s)][len(t)]

























"""Solution 1:
"""
# 解题思路：这道题不只像word break那样判断是否可以分割，而且要找到所有的分割方式，那么我们就要考虑dfs了。
# 不过直接用dfs解题是不行的，为什么？因为决策树太大，如果全部遍历一遍，时间复杂度太高，无法通过oj。
# 那么我们需要剪枝，如何来剪枝呢？使用word break题中的动态规划的结果，在dfs之前，先判定字符串是否可以被分割，
# 如果不能被分割，直接跳过这一枝。实际上这道题是dp+dfs。
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def check(self,s,dict):
    	dp = [False for i in range(len(s)+1)]
    	dp[0] = True
    	for i in range(1,len(s)+1):
    		for k in range(0,i):
    			if dp[k] and s[k:i] in dict:
    				dp[i] = True
    	return dp[len(s)]

    def dfs(self,s,dict,value):
    	if self.check(s,dict):
    		if len(s)==0:
    			Soluiton.res.append(value[1:])
    		for i in range(1,len(s)+1):
    			if s[:i] in dict:
    				self.dfs(s[:i],dict,value+' '+s[:i])

    def wordBreak(self, s, wordDict):
    	Solution.res = []
    	self.dfs(s,dict,'')
    	return Solution.res


 """Solution 2: Recrusive
 	解题思路：记忆化搜索
	在搜索过程中，使用字典tokenDict (d) 将已经搜索过的子句的拆解方案记录下来，从而实现DFS的剪枝。
 """
 class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
    	d = dict()
    	def dfs(s):
    		ans = []
    		if s in wordDict:
    			ans.append(s)
    		for i in range(1,len(s)):
    			prefix, suffix = s[:i],s[i:]
    			if prefix not in wordDict:
    				continue
    			res = []
    			if suffix in d:
    				rest = d[suffix]
    			else:
    				rest = dfs(suffix)
    			for n in rest:
    				ans.append(prefix+' '+n)
    		d[s] = ans
    		return ans
    	return dfs(s)































        
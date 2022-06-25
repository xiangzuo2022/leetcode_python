
"""recursive, "*" 可以重复前面的字符0次或多次
"""
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
    	
        return self.isMatch_rec(s[::-1], p[::-1])  # ?? 为何倒过来？
 
    def isMatch_rec(self, s, p):
        if not p:
            return s == ''
        elif s and (p[0] == s[0] or p[0] == '.'):
        	#print s[1:], p[1:]
           	return self.isMatch_rec(s[1:], p[1:])
        elif p[0] == '*':
            if s and (p[1] == '.' or s[0] == p[1]):
                return self.isMatch_rec(s, p[2:]) or self.isMatch_rec(s[1:], p)
            else:
                return self.isMatch_rec(s, p[2:])
        return False



"""DP
"""
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]


if __name__ == '__main__':
	a = Solution()
	print a.isMatch("ab","a*")
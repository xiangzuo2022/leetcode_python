class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        max_s = ''
        for i in xrange(len(s)):
            s1 = self.extend(s, i)
            if len(s1) > len(max_s):
                max_s = s1
            s2 = self.extend(s, i, i+1)
            if len(s2) > len(max_s):
                max_s = s2
        return max_s
 
    def extend(self, s, i, j=None):
        if j:
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
            return s[i+1:j]
        else:
            j, k = i - 1, i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j, k = j - 1, k + 1
            return s[j+1:k]
    	


"""
方法三：中心扩散法
O(n*n)。对于每一个字符，以之作为中间元素往左右寻找。注意处理奇偶两种模式：
1. aba
2. abba
"""
def longestPalindrome(self, s):
    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]

### DP 解法
第 1 步：定义状态
dp[i][j] 表示子串 s[i, j] 是否为回文子串。

第 2 步：思考状态转移方程
这一步在做分类讨论（根据头尾字符是否相等），根据上面的分析得到：

dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2:
            return s
        dp = [[False for i in range(n)] for j in range(n)]
        
        max_len = 1
        start = 0
        
        for i in range(n):
            dp[i][i] = True
            
        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                    
                if dp[i][j]:
                    curr_len = j-i+1
                    if curr_len > max_len:
                        max_len = curr_len
                        start = i
        return s[start:start+max_len]
    

# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=47
# DP 中心扩散法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(len(s)):
            # aba case
            temp = helper(i, i)
            if len(temp) > len(res):
                res = temp
            # abba case
            temp = helper(i, i+1)
            if len(temp) > len(res):
                res = temp
        return res




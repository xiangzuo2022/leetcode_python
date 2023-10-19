思路:
动态规划

dp[i]到字符串第i位置最多解码的个数

动态方程: dp[i] = dp[i-1] + dp[i - 2]

注意:这里有很多要考虑的情况

例如:101,100,所以要考虑有0的情况,直接看代码,注释写在里面了!

再附上自顶向下的动态规划,

作者：powcai
链接：https://leetcode-cn.com/problems/decode-ways/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-4/
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        # 考虑第一个字母
        if s[0] == "0":
            return 0
        else:
            dp[0] = 1
        if len(s) == 1: return dp[-1]
        # 考虑第二个字母
        if s[1] != "0":
            dp[1] += 1
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, len(s)):
            # 当出现连续两个0
            if s[i - 1] + s[i] == "00": return 0
            # 考虑单个字母
            if s[i] != "0":
                dp[i] += dp[i - 1]
            # 考虑两个字母
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]

一种递归的解法， 本质是两位一看。
比较喜欢这种解法
class Solution:
    @functools.lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        ans = 0
        if len(s) >= 1 and s[0] != '0':
            ans += self.numDecodings(s[1:])
        if len(s) >= 2 and s[0] != '0' and int(s[:2]) <= 26:
            ans += self.numDecodings(s[2:])
        return ans

作者：powcai
链接：https://leetcode-cn.com/problems/decode-ways/solution/zi-di-xiang-shang-he-zi-ding-xiang-xia-by-powcai-4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
DP 解法 official solution
like this solution
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]
      
"""
注意到在状态转移方程中，f_ifi
​
  的值仅与 f_{i-1}f 
i−1
​
  和 f_{i-2}f 
i−2
​
  有关，因此我们可以使用三个变量进行状态转移，省去数组的空间。

"""
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # a = f[i-2], b = f[i-1], c = f[i]
        a, b, c = 0, 1, 0
        for i in range(1, n + 1):
            c = 0
            if s[i - 1] != '0':
                c += b
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                c += a
            a, b = b, c
        return c

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/decode-ways/solution/jie-ma-fang-fa-by-leetcode-solution-p8np/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/decode-ways/solution/jie-ma-fang-fa-by-leetcode-solution-p8np/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# https://www.youtube.com/watch?v=6aEyTjOwlJU&t=6s
# 分析清楚几种case就好
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i+1)
            if (i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                res += dfs(i+2)
            dp[i] = res 
            return res
        return dfs(0)
    
# buttom up DP
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        
        for i in range(len(s)-1,-1,-1):            
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if (i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                dp[i] += dp[i+2]
        return dp[0]
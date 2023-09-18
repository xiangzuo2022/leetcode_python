class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        n = len(s)
        if n < 2: return 1
        def helper(s, left, right):
            counter = 0            
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                counter += 1
            return counter
        for i in range(n):
            l1 = helper(s, i, i) 
            l2 =  helper(s, i, i+1)
            ans += l1 + l2
        return ans

此处撰写解题思路
回文字符串的长度可能为单数，也可能为双数，所以要分两种情况去解决。
我们可以首先找到这个回文字符串的中心字符，如果字符串的长度为奇数，那么中心字符一定存在，如果为偶数，那么中心字符存在两个，分别在i和i+1，两个指针分别对应字符串的首位依次++和--，如果情况满足，那么结果+1，否则，退出循环。看代码一眼就懂了哦。

作者：uYGN9I8C6N
链接：https://leetcode-cn.com/problems/palindromic-substrings/solution/bi-jiao-jian-dan-de-suan-fa-by-uygn9i8c6n/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
动态规划的解法
整体上是两种，就是s[i]与s[j]相等，s[i]与s[j]不相等这两种。
当s[i]与s[j]不相等，那没啥好说的了，dp[i][j]一定是false。
当s[i]与s[j]相等时，这就复杂一些了，有如下三种情况
情况一：下标i 与 j相同，同一个字符例如a，当然是回文子串
情况二：下标i 与 j相差为1，例如aa，也是文子串
情况三：下标：i 与 j相差大于1的时候，例如cabac，此时s[i]与s[j]已经相同了，我们看i到j区间是不是回文子串就看aba是不是回文就可以了，
那么aba的区间就是 i+1 与 j-1区间，这个区间是不是回文就看dp[i + 1][j - 1]是否为true。
如果这矩阵是从上到下，从左到右遍历，那么会用到没有计算过的dp[i + 1][j - 1]，也就是根据不确定是不是回文的区间[i+1,j-1]，来判断了[i,j]是不是回文，
那结果一定是不对的。
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s)-1, -1, -1): #注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1: #情况一 和 情况二
                        result += 1
                        dp[i][j] = True
                    elif dp[i+1][j-1]: #情况三
                        result += 1
                        dp[i][j] = True
        return result
"""
动态规划简洁版
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s)-1, -1, -1): #注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]): 
                    result += 1
                    dp[i][j] = True
        return result
    

# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=47
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 2: return 1
        ans = 0

        def helper(l, r):
            counter = 0
            while l >=0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                counter += 1
            return counter

        for i in range(n):
            l1 = helper(i, i)
            l2 = helper(i, i+1)
            ans += l1 + l2
        return ans
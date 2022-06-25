"""
方法一：按字符分组
思路与算法
我们可以将字符串 ss 按照 00 和 11 的连续段分组，存在 \textit{counts}counts 数组中，例如 s = 00111011s=00111011，可以得到这样的 \textit{counts}counts 数组：\textit{counts} = \{2, 3, 1, 2\}counts={2,3,1,2}。

这里 \textit{counts}counts 数组中两个相邻的数一定代表的是两种不同的字符。假设 \textit{counts}counts 数组中两个相邻的数字为 uu 或者 vv，它们对应着 uu 个 00 和 vv 个 11，或者 uu 个 11 和 vv 个 00。它们能组成的满足条件的子串数目为 \min \{ u, v \}min{u,v}，即一对相邻的数字对答案的贡献。

我们只要遍历所有相邻的数对，求它们的贡献总和，即可得到答案。
"""
class Solution(object):
    def countBinarySubstrings(self, s):
        groups = [1]
        for i in xrange(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in xrange(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
      
      
"""
上面这个实现的时间复杂度和空间复杂度都是 O(n)O(n)。

对于某一个位置 ii，其实我们只关心 i - 1i−1 位置的 \textit{counts}counts 值是多少，所以可以用一个 \textit{last}last 变量来维护当前位置的前一个位置，这样可以省去一个 \textit{counts}counts 数组的空间。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/count-binary-substrings/solution/ji-shu-er-jin-zhi-zi-chuan-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class Solution(object):
    def countBinarySubstrings(self, s):
        ans, prev, cur = 0, 0, 1
        for i in xrange(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)
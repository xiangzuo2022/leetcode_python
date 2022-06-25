"""
这里我们可以利用只有一个不同的特点在O(N)时间内完成。如果两个字符串只有一个编辑距离，则只有两种情况：
两个字符串一样长的时候，说明有一个替换操作，我们只要看对应位置是不是只有一个字符不一样就行了
一个字符串比另一个长1，说明有个增加或删除操作，我们就找到第一个对应位置不一样的那个字符，
如果较长字符串在那个字符之后的部分和较短字符串那个字符及之后的部分是一样的，则符合要求
如果两个字符串长度差距大于1，肯定不对
"""
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        if m > n: # only consider n is the larger one's case
            return self.isOneEditDistance(t, s)
        if n - m > 1 or s == t:
            return False
        for i in range(m):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:]
        return True

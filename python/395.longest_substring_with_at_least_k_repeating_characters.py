"""
思路： 
题目要求 满足串中每个字符出现次数都不少于k次的最长子串。
首先出现小于k次的字符一定不会出现在要求的子串中，因此统计字符串中每个字符出现的次数，以小于k次的字符为分割点，
将字符串分割为几个小片段。对每个小片段，我们仍需要判断它是否满足每个字符出现次数不小于k，所以对每个小片段递归分割。
终止条件是片段中每个字符次数都不小于k时返回片段长度。
"""

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


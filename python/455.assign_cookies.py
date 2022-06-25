"""
greedy algorithm: see leetcode 101
"""
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
    
        m, n = len(g), len(s)
        i, j = 0, 0
        g.sort()
        s.sort()
        while i < m and j < n:
            if s[j] >= g[i]:               
                i += 1
            j += 1
        return i
      
      
      
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        for i in range(len(s)):
            if res <len(g) and s[i] >= g[res]:  #小饼干先喂饱小胃口
                res += 1
        return res
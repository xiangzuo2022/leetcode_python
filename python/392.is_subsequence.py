"""
解题思路：利用队列（Queue）数据结构。
将s加入队列，遍历t，当t的当前字符c与队头相同时，将队头弹出。
最后判断队列是否为空即可。
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        queue = collections.deque(s)
        for c in t:
            if not queue: return True # if no check: IndexError: deque index out of range
            if c == queue[0]:
                queue.popleft()
        return not queue


常规双指针解法
# @author:leacoder 
# @des:  双指针解法 判断子序列

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    	# 判断 s 是否为 t 的子序列。
    	# 指针 point_s 指向 s 第一个字符，指针 point_t 指向 t 第一个字符。逐一判断 point_s 所指向的字符是否在 t 中存在。
    	point_s = 0
    	point_t = 0
    	length_s = len(s)
    	length_t = len(t)
'''
1、如果 s[point_s] != t[point_t] , point_t = point_t + 1, 继续对比t的下一个字符，s的第point_s个字符是否在t中
2、如果 s[point_s] == t[point_t] , point_s = point_s + 1 , point_t = point_t + 1, 继续对比s的下一个字符。
'''
    	while point_s < length_s and point_t < length_t:
    		if s[point_s] == t[point_t]:
    			point_s = point_s + 1
    		point_t = point_t + 1
    	# 最后通过point_s是否与length_s相等判断s 是否为 t 的子序列。
    	return point_s == length_s



class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        point_s = point_t = 0
        m, n = len(s), len(t)
        while point_s < m and point_t < n:
            if s[point_s] == t[point_t]:
                point_s += 1
            point_t += 1
        return point_s == m
      
"""
递归解法累死1143
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s) + 1
        n = len(t) + 1
        dp = [[0]*n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        return len(s) == dp[-1][-1]
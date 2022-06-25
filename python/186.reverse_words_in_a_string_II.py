"""
先把每个单词翻转一遍，再把整个字符串翻转一遍，或者也可以调换个顺序，先翻转整个字符串，再翻转每个单词
"""


class Solution(object):
    def reverseWords(self, s):
        self.reverse(s, 0, len(s) - 1)

        beg = 0
        for i in xrange(len(s)):
            if s[i] == ' ':
                self.reverse(s, beg, i-1)
                beg = i + 1
            elif i == len(s) - 1:
                self.reverse(s, beg, i)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def reverse(str, start, end):
            while start < end:
                str[start], str[end] = str[end], str[start]
                start += 1
                end -= 1

        n = len(str)
        beg = 0
        reverse(str, 0, n-1)  # reverse the whole array first
        for i in range(n):
            if str[i] == ' ':
                reverse(str, beg, i-1)
                beg = i + 1
            elif i == n-1:  # the last word cannot use ' ' to reverse, so we need to deal with it seperately.
                reverse(str, beg, i)

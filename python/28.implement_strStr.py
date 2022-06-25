"""此题估计是facebook面试题， 考查的是haystack结构
"""

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    # 题意：实现字符串匹配函数，并返回一个指针，这个指针指向原字符串中第一次出现待匹配字符串的位置。
    # 如：haystack='aabbaa'; needle='bb'。如果使用python实现，则最后返回的应该是一个字符串，
    # 即：'bbaa'。
    def strStr(self, haystack, needle):

        if haystack == needle == '':
            return 0
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:i  +n] == needle:
                return i

        return -1


# ****************** The Second Time ************
"""
# Solution: Brute Force
# 题意：实现字符串匹配函数，并返回一个指针，这个指针指向原字符串中第一次出现待匹配字符串的位置。
# 如：haystack='aabbaa'; needle='bb'。如果使用python实现，则最后返回的应该是一个字符串，即：'bbaa'。
"""

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if haystack == needle == '':
            return 0
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:  # because of here counts to n thus the above line needs to substract n
                return i 
        return -1

"""
另一种写法， 不够简洁
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        n = len(haystack)
        m = len(needle)
        i = 0
        while i+m-1 < n:

            if haystack[i] == needle[0] and ''.join(haystack[i:i+m]) == needle:
                return i
            else:
                i += 1

        return -1
                    


"""
暴力解法
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:
                return i
        return -1

"""
KMP解法
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        lnd = len(needle)
        lnf = len(haystack)
        if lnd > lnf: return -1

        # 偏移表预处理    
        dic ={v:lnd-k for k,v in enumerate(needle)}
        idx = 0

        while idx+lnd <= lnf:
            # 待匹配字符串
            str_cut = haystack[idx:idx+lnd]
            # 判断是否匹配
            if str_cut == needle:
                return idx
            elif idx+lnd == lnf:
                return -1
            else:
                # 不匹配情况下，根据下一个字符的偏移，移动idx
                nextc = haystack[idx+lnd]
                idx += dic[nextc] if dic.get(nextc) else lnd+1
        return -1










                    

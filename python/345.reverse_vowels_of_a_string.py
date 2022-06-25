"""
这道题让我们翻转字符串中的元音字母，元音字母有五个a,e,i,o,u，需要注意的是大写的也算，
所以总共有十个字母。我们写一个isVowel的函数来判断当前字符是否为元音字母，
如果两边都是元音字母，那么我们交换，如果左边的不是，向右移动一位，如果右边的不是，
则向左移动一位.
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = 'AEIOUaeiou'
        s = list(s)
        i, j = 0, len(s)-1
        while i < j:
            while s[i] not in vowel and i < j:
                i = i + 1
            while s[j] not in vowel and i < j:
                j = j - 1
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
        return ''.join(s)

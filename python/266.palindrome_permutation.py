"""
这种方法用到了一个set，我们遍历字符串，如果某个字母不在set中，我们加入这个字母，如果字母已经存在，我们删除该字母，
那么最终如果set中没有字母或是只有一个字母时，说明是回文
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = set()
        for i in s:
            if i not in t:
                t.add(i)
            else:
                t.remove(i)
        if len(t) == 0 or len(t) == 1:
            return True
        return False

"""
解法二：这道题让我们判断一个字符串的全排列有没有是回文字符串的，那么根据题目中的提示，我们分字符串的个数是奇偶的情况来讨论，
如果是偶数的话，由于回文字符串的特性，每个字母出现的次数一定是偶数次，当字符串是奇数长度时，只有一个字母出现的次数是奇数，
其余均为偶数，那么利用这个特性我们就可以解题，我们建立每个字母和其出现次数的映射，然后我们遍历哈希表，统计出现次数为奇数的字母的个数，
那么只有两种情况是回文数，第一种是没有出现次数为奇数的字母，再一个就是字符串长度为奇数，且只有一个出现次数为奇数的字母，
"""
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        for item in s:
            dic[item] = dic.get(item, 0) + 1
        return sum(v % 2 for v in dic.values()) < 2
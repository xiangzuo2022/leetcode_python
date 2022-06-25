"""
本题要找到数组中两个最长的且没有公共字母的字符串。如果有暴力解法，时间复杂度过高，而且代码也不简洁。
因为每个字符串都是由26个字母组成的，所以我们可以考虑先对每个字符串编码，可以利用位运算进行编码，出现的字母对应位置一。
然后判断两个字符串有没有公共字符只需判断它们对应的编码的与运算是否为1即可。

"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        nums = []
        size = len(words)
        for w in words:
            nums += sum(1 << (ord(x) - ord('a')) for x in set(w)), ???
        ans = 0
        for x in range(size):
            for y in range(size):
                if not (nums[x] & nums[y]): # check no same letters
                    ans = max(len(words[x]) * len(words[y]), ans)
        return ans


""""
a direct solution
""""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_dict = dict()
        for word in words:
            word_dict[word] = set(word)
        max_len = 0
        for i1, w1 in enumerate(words):
            for i2 in range(i1+1, len(words)):
                w2 = words[i2]
                if not (word_dict[w1] & word_dict[w2]):
                    max_len = max(max_len, len(w1) * len(w2))
        return max_len
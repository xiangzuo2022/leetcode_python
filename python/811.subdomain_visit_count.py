"""
这道题让我们统计子域名的访问量，所谓的子域名，就是一个完整的域名以点断开的，每个断开的地方到末尾之间的子字符串就是一个子域名，
现在给了我们很多完整域名的访问量，让我们统计所有子域名的访问量，题目中给的例子很好的说明了问题。那么这种统计字符串出现个数的问题，
我们应该不难想到需要用一个HashMap来建立字符串和其出现次数的映射。那么接下来要做的就是将每一个全域名提取出来，然后拆分成子域名。
提取全域名操作不难，因为给的格式都是一样的，前面是数字，中间一个空格，后面是全域名。我们只需要找到空格的位置，前面的部分转为整型数cnt，
后面的就是全域名了。取出全域名之后就要进行拆分成子域名了，我们可以进行遍历，每当找到小数点的位置时，将后面的子字符串的映射值增加cnt，
以此类推直到拆完所有的子域名。注意之前的全域名的映射值别忘了也要加上cnt，最后的最后我们只要将HashMap中的映射对组成题目中要求返回的格式即可.
"""
import collections
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count = collections.Counter()
        for cp in cpdomains:
            c, d = cp.split()
            count[d] += int(c)
            for i in range(len(d)):
                if d[i] == '.':
                    count[d[i + 1:]] += int(c)
        return ["%d %s" % (count[k], k) for k in c]

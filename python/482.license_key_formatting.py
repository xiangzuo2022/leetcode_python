class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-','')[::-1]
        n = len(S)
        res = ''
        for i in range(n):
            if (i % K) or i == 0:
                res = S[i] + res
            else:
                res = S[i] + "-" + res
        return res

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # 逆序思维，假如题目中第一组的条件是用在最后一组，是不是很容易做：遇到合适索引就拼接-
        # 所以本题将字符串翻转一下，然后每次换成前插就好了
        s = S.upper().replace('-','')[::-1]
        res = ''
        for i in range(len(s)):
            if i%K == 0 and i!=0: res = '-' + res
            res = s[i] + res
        return res

作者：niu-meng
链接：https://leetcode-cn.com/problems/license-key-formatting/solution/ni-xu-jian-ji-dai-ma-by-niu-meng/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
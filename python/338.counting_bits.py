"""
倒过来想，一个数 * 2 就是把它的二进制全部左移一位，也就是说 1的个数是相等的。
那么我们可以利用这个结论来做。res[i /2] 然后看看最低位是否为1即可（上面*2一定是偶数，
这边比如15和14除以2都是7，但是15时通过7左移一位并且+1得到，14则是直接左移）
所以res[i] = res[i >>1] + (i&1).
"""


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0] * (num + 1)
        for i in range(1, num+1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans

"""
对于所有的数字，只有两类：
奇数：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。
偶数：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。因为最低位是 0，除以 2 就是右移一位，也就是把那个 0 抹掉而已，所以 1 的个数是不变的。
https://leetcode-cn.com/problems/counting-bits/solution/hen-qing-xi-de-si-lu-by-duadua/
"""
# n log(n)
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0] * (num+1)
        for i in range(1, num+1):
            if i % 2 == 1:
                bits[i] = bits[i-1] + 1
            else:
                bits[i] = bits[i//2] # floor division
        return bits
    
# https://www.youtube.com/watch?v=RyBM56RIWrM
# DP
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
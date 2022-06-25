# 以下方法用到了额外的memory, is not the best solution
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, A):
        dict = {}
        for i in range(len(A)):
            if A[i] not in dict:
                dict[A[i]] = 1
            else:
                dict[A[i]] += 1
        for word in dict:
            if dict[word] == 1:
                return word


                
if __name__ == '__main__':
	a = Solution()
	print a.singleNumber([2,2,3,2])



# ******* The Second Time *********
"""
#  http://www.cnblogs.com/zuoyuan/p/3719753.html
#  http://liangjiabin.com/blog/2015/03/leetcode-single-number-ii-in-python.html
解题思路：这道题就比较难了。也是考察位操作。网上的位操作解法看了好半天也没有得其精髓。由于序列中除了那唯一的一个
数之外所有的数都是三个三个出现的。如果把这些数都转换成二进制，那么二进制数中1的那些位会连续出现三次，我们可以利
用这个思路来解题。比如：3331222转换成二进制为：11 11 11 01 10 10 10。在第1位上，1出现了4次。第2位上，
1出现了6次。那么我们把每一位上为1的个数mod 3剩下的1就是我们所求的数，比如这个例子：4 mod 3 = 1; 
6 mod 3 = 0。这样剩下的二进制位为：01。那最后所求的数就是1了。那怎么实现这个想法呢？使用二进制模拟三进制。
在连续来3个1后清0。使用两个bit位，bit1和bit2。初始状态bit1和bit2都是0，即00，在来了第一个1后，变成了01，
来了第二个1后变成了10，来了第三个1后，变成了11，然后清0为00，即：00->01->10->11，然后将11清为00，
这个过程就是我们编程的思路。比如如果输入序列为：1 1 1 1 1 1 1，则变化过程为：
00->01->10->11->00->01->10->11->00->01，最后剩下的是1，也就得到了结果。如果位数多那么以此类推，
比如序列为：3 3 3 2 2 2 1。则二进制为：11 11 11 10 10 10 01。则低位为1 1 1 0 0 0 1，
变化过程为：00->01->10->11->00->00->00->00->01，所以低位剩下1。高位为：1 1 1 1 1 1 0，
变化过程为：00->01->10->11->00->01->10->11->00->00，所以高位剩下0。那么最后剩下的是01，也就是1。
如果位数更多，可以以此类推。程序中的one相当于bit1，two相当于bit2。
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        one = 0; two = 0; three = 0
        for i in range(len(nums)):
            two |= nums[i] & one
            one = nums[i] ^ one
            three = ~(one & two)
            one &= three
            two &= three
        return one
"""
因为题目已经说了，除了一个数字以外，其他的都出现了3次，如果我们把那个特殊的数剔除，并把剩下的数于每一位来
加和的话，每一位上1出现的次数必然都是3的倍数。所以，解法就在这里，将每一位数字分解到32个bit上，
统计每一个bit上1出现的次数。最后对于每一个bit上1出现的个数对3取模，剩下的就是结果。
"""

class Solution(object):
    def singleNumber(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit = [0 for i in xrange(32)]
        # bit[0] is the least significant bit, bit[0]是最低位
        for number in A:
            for i in xrange(32):
                if (1 << i) & number == 1 << i: bit[i] += 1
        res = 0
        if bit[31] % 3 == 0: # target number is positive
            for i in xrange(31):
                if bit[i] % 3 == 1: res += 1 << i
        else: # target number is negative
            for i in xrange(31):
                if bit[i] % 3 == 0: res += 1 << i # now res = 11..11 - y
            res = -(res + 1) # now res = -(11..11 - y + 1) = x
        return res


###  my own solution 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit = [0]*32; ans = 0
        for e in nums:
            for i in range(32):
                if (1<<i) & e == 1<<i:  # i<<1 就是用于一位一位的操作
                    bit[i] += 1
        if bit[31]%3 == 0:   # 符号位也出现了3次(正数)
            for i in range(31):
                if bit[i]%3 == 1:
                    ans |= 1<<i  # again i<<1 就是用于一位一位的操作
        else:
            for i in range(31):
                if bit[i]%3 == 0:  # 负数是0 不是 1
                    ans |= 1 << i
            ans = -(ans+1)
        return ans



"""
思想来自九章的java程序， 但是python要自己转换正负数
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return -1
        result = 0
        bit = [0]*32
        for i in range(32):
            for e in nums:
                bit[i] += e >> i & 1
                bit[i] %= 3
            result |= (bit[i] << i)
        return self.convert(result)
    
    def convert(self,x):  # comes from the discussion solution
        if x >= 2**31:
            x -= 2**32
        return x

"""
similar solution
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in xrange(0,32):
            count = 0
            for a in nums:
                if ((a >> i) & 1):
                    count+=1
            ans |= ((count%3) << i)
        return self.convert(ans)
    
    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x


























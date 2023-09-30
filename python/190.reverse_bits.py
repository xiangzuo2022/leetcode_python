class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	x = bin(n)[:1:-1].ljust(32,'0')  # move to left by 32 bits    	
        return int(x, base = 2)




# ********The Second Time ************
"""
# [分析]
# 最笨的解法就是每次移位，这样的话不管是多少个1，都要循环执行32次。比较巧妙的解法可以将循环次数减少到与1的个数
# 一样。利用的性质就是n－1之后，n最低位的1之后（包括其本身）的所有bits翻转。
# 此题有更优解
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	ans = 0
    	for i in range(32):            
    		ans = (ans<<1) | (n & 1)  #?? n & 1
    		n >>= 1  # 十进制转二进制
    	return ans


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32): 
            ans <<= 1           
            ans = | (n & 1)  # 末尾为1的被保留
            n >>= 1  # 移调最末尾一位
        return ans

# https://www.youtube.com/watch?v=UcoN6UjAI64
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res



if __name__ == '__main__':
	a = Solution()
	n = 43261596
	print a.reverseBits(n)












"""
题目大意：
给定一个整数n，返回n!（n的阶乘）数字中的后缀0的个数。
# 此题解法不好想， 记住即可！！！
# Solution: O（logn）解法：
# 一个更聪明的解法是：考虑n!的质数因子。后缀0总是由质因子2和质因子5相乘得来的。如果我们可以计数2和5的
# 个数，问题就解决了。考虑下面的例子：
# n = 5: 5!的质因子中 (2 * 2 * 2 * 3 * 5)包含一个5和三个2。因而后缀0的个数是1。
# n = 11: 11!的质因子中(2^8 * 3^4 * 5^2 * 7)包含两个5和三个2。于是后缀0的个数就是2。
# 我们很容易观察到质因子中2的个数总是大于等于5的个数。因此只要计数5的个数就可以了。那么怎样计算n!的
# 质因子中所有5的个数呢？一个简单的方法是计算floor(n/5)。例如，7!有一个5，10!有两个5。除此之外，
# 还有一件事情要考虑。诸如25，125之类的数字有不止一个5。例如，如果我们考虑28!，我们得到一个额外的5，
# 并且0的总数变成了6。处理这个问题也很简单，首先对n÷5，移除所有的单个5，然后÷25，移除额外的5，以此类推。下面是归纳出的计算后缀0的公式。
# http://bookshadow.com/weblog/2014/12/30/leetcode-factorial-trailing-zeroes/
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
    	x = 5
    	ans = 0
    	while n >=x:
    		ans += n/x
    		x*=5
    	return ans

    """
    计算包含的2和5组成的pair的个数就可以了，一开始想错了，还算了包含的10的个数。  
    因为5的个数比2少，所以2和5组成的pair的个数由5的个数决定。  
    观察15! = 有3个5(来自其中的5, 10, 15)， 所以计算n/5就可以。  
    但是25! = 有6个5(有5个5来自其中的5, 10, 15, 20, 25， 另外还有1个5来自25=(5*5)的另外一个5），  
    所以除了计算n/5， 还要计算n/5/5, n/5/5/5, n/5/5/5/5, ..., n/5/5/5,,,/5直到商为0。 
    """

     def trailingZeroes(self, n):
        count = 0
        while n > 0:
            k = n/5
            count += k
            n = k
        return count

        


    # def factorial(self,n):
    # 	if n==0:
    # 		return 1
    # 	else:
    # 		return n*self.factorial(n-1)
"""
O(n)解法， 产生Time Limit Exceeded
"""
class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        f = 1
        for i in range(1,n+1):
            f *= i
        count = 0
        while f%10 == 0:
            count += 1
            f = f/10
            if f%10:
                break
        return count




if __name__ == '__main__':
	a = Solution()
	print a.factorial(3)

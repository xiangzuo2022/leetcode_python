"""
解题思路：
模拟题，循环过程中用set记录每次得到的平方和当出现非1的重复平方和时，返回False
否则，返回True.
此代码非常简洁
"""
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        numSet = set()    #用list也可以, 用来判断有没有重复值出现
        while n != 1 and n not in numSet:
            numSet.add(n)
            sum = 0
            while n:
                digit = n % 10
                sum += digit * digit
                n /= 10
            n = sum
        return n == 1  	

"""
这道题目使用哈希法，来判断这个sum是否重复出现，如果重复了就是return false， 否则一直找到sum为1为止。
判断sum是否重复出现就可以使用unordered_set。
还有一个难点就是求和的过程，如果对取数值各个位上的单数操作不熟悉的话，做这道题也会比较艰难。
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        set_ = set()
        while 1:
            sum_ = self.getSum(n)
            if sum_ == 1:
                return True
            #如果这个sum曾经出现过，说明已经陷入了无限循环了，立刻return false
            if sum_ in set_:
                return False
            else:
                set_.add(sum_)
            n = sum_
            
    #取数值各个位上的单数之和
    def getSum(self, n):
        sum_ = 0
        while n > 0:
            sum_ += (n%10) * (n%10)
            n //= 10
        return sum_

  



if __name__ == '__main__':
	s = Solution()
	n = 18
	print s.isHappy(n)
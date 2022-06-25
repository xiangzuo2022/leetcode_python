
from math import sqrt

class Solution:  # 筛选法
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:  # no prime
            return 0        
        is_prime = [True] * n               
        num = 0
        for i in xrange(2, n):
            if is_prime[i]:
               num += 1
               for j in xrange(i+i, n, i):
                   is_prime[j] = False
                   
        return num




class Solution:  # O(n^2) Time limit exceeded
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
      def isPrime(a):
        for i in range(2,n):
          if a % i != 0:
            return False
        return True

      count = 0
      for j in range(2,n):
        if isPrime(j) == True:
          count += 1
      return count


"""
质数（prime number）又称素数，有无限个。一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除
2 is prime, 0 and 1 are not primes.
埃拉托斯特尼筛法 O(nlogn)
首先我们把所有的数标记为素数（true），就是我们从2开始，找出所有2的倍数，把它标记为不是素数（false）
(当然不是素数),再找到3，找出所有3的倍数，也标记为不是素数（false），再找到下一个标记为（true）的数k，
再去找到所有k的倍数，标记为（false），依次类推...那么剩下来的数就都是素数了.
"""
class Solution:  # 筛选法
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 2: return 0
        isPrime = [True]*n;count = 0
        for i in range(2,n):
            if isPrime[i] == True:
                count += 1
                for j in xrange(i+i,n,i):
                    isPrime[j] = False
        return count


class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 2:
          return 0
        isPrime = [True]*n;count = 0
        for i in range(2,n):
            if isPrime[i] == True:
                count += 1
                for j in xrange(i+i,n,i):
                    isPrime[j] = False
        return count








# prime: a number is not divisible by any number less than n
# 采用Eratosthenes筛选法，依次分别去掉2的倍数，3的倍数，5的倍数，……，最后剩下的即为素数。
# 除了自身之外，无法被其它整数整除的数称之为质数，要求质数很简单，但如何快速的求出质数则一直是程式设计人员
# 与数学家努力的课题， 在这边介绍一个着名的 Eratosthenes求质数方法。

# 解法:
# 首先知道这个问题可以使用回圈来求解，将一个指定的数除以所有小于它的数，若可以
# 整除就不是质数，然而如何减少回圈的检查次数？如何求出小于N的所有质数？
# http://www.cnblogs.com/color-my-life/p/3265236.html

质数（prime number）又称素数，有无限个。一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除
2 is prime








    


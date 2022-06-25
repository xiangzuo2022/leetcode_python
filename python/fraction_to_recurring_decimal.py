"""
# ******** The Second Time *******
# 解题的关键是当余数开始循环时，得数也会开始循环。
# 你需要用一个哈希表存储：key = 余数， value = 当前数位在小数得数中的位置。一旦找到重复的余数，
# 就可以通过查找哈希表获得循环节的起点，从而得到小数的循环节。
# 执行除法的过程中，余数可能变为0。此时说明小数是有限小数，可以立即返回得数。
# 不要忘了考虑负数的情况
用/ instead of //也能通过；
"""
 class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        n = numerator; d = denominator
        res = ''
        if n%d == 0:
            return str(n//d)  # // Floor division. Division that returns the integer of the 
                              #  division with no decimal remainder. 
        if n*d < 0:
            res += '-'
        n = abs(n); d= abs(d)
        res += str(n//d) +'.'
        n %= d
        i = len(res)
        dd = {}
        while n != 0:
            if n not in d:
                dd[n] = i # 哈希表存储余数及其位置
            else:
                i = dd[n] # 重复的余数的位置
                res = res[:i] + '('+res[i:]+')'
                return res
            n *= 10  # 余数扩大10倍再与被除数运算, 和手算是一样的
            res+= str(n//d)
            n%=d
            i+=1
        return res

















数学题， 找规律
写下前几个，就能看出规律了。

n=1: res=10

n=2: res=9*9+10=91 # 两位数第一位只能为1-9，第二位只能为非第一位的数，加上一位数的所有结果

n=3: res=9 * 9 * 8+91=739 # 三位数第一位只能为1-9，第二位只能为非第一位的数，第三位只能为非前两位的数，加上两位数的所有结果

n=4: res=9 * 9 * 8 * 7+739=5275 # 同上推法

 def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        res, muls = 10, 9
        for i in range(1, min(n,10)):
            muls *= 10 - i
            res += muls
        return res

作者：yybeta
链接：https://leetcode-cn.com/problems/count-numbers-with-unique-digits/solution/pai-lie-zu-he-zhi-shi-pythonshuang-100shi-xian-by-/


Also pass
另：n大于10无意义，因为十个数字都用了
n>10以后答案都不变了，因为11位数不可能各个位数都不同，因此 i 遍历1到min(n, 10)即可
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n: return 1
        res = 10
        mul = 9
        for i in range(1, n):
            mul *= 10 - i
            res += mul
        return res
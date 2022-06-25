class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
    	integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        numerals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res = ''
        for i in range(len(integers)):
            num, remainder = divmod(num, integers[i])
            res+=num*numerals[i]
            num = remainder

        return res
# 规律就是1,4,5,9,10然后每次十倍循环。算法就是给一个数，大于1000的时候就写上一个M
 #, 还大于1000，再写一个M… 终于小于1000了，看看大于900不？，大于500不…如此类

if __name__ == '__main__':
	a = Solution()
	print a.intToRoman(900)

# ******** The Secon Time *************
"""
# 解题思路：整数（1~3999）到罗马数字的转换。字母前置表示减法，例如CM表示M-C=1000-100=900，
# XL表示L-X=50-10=40。
# 规律就是1,4,5,9,10然后每次十倍循环。算法就是给一个数，大于1000的时候就写上一个M
# 还大于1000，再写一个M… 终于小于1000了，看看大于900不？，大于500不…如此类
# 记住既可以了
"""

class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        numerals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        ans = ''
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                ans += numerals[i]
        return ans

























 
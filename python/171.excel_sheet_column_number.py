"""
# Solution: 解题思路：26进制转化为10进制
# 大小写字母之间的ASCII码差距是一个常量,小写字母的ASCII码大于大写字母的ASCII码,因此
# 小写字母的ASCII码减去这个常量即变成对应的大写字母[小字母变成大写字母方法之一]
使用ord()函数将字母转化为整数，使用chr()函数将整数转化回字母

有些题就是通过观察找规律
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
    	ans = 0
    	for e in s:
    		ans = ans * 26 + ord(e) - ord('A') + 1
    	return ans




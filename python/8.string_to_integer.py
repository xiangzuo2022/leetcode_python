

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):    	
		str = str.strip()
		newStr = []
		for i in xrange(len(str)):
			if '0' <= str[i] <= '9' or (str[i] in ('+', '-') and i == 0):
				newStr.append(str[i])
			else:
				break
	   	if newStr in ([], ['+'], ['-']):
	   		return 0
	   	elif -2147483648 <= int(''.join(newStr)) <= 2147483647:
	   		return int(''.join(newStr))
	   	elif int(''.join(newStr)) > 2147483647:
	   		return 2147483647
	   	else:
	   		return -2147483648



# *************** The Second Time ****************
"""
# Solution: the key point is to deal with different input cases.
# 1. 首先需要丢弃字符串前面的空格；
# 2. 然后可能有正负号（注意只取一个，如果有多个正负号，那么说这个字符串是无法转换的，返回0。
#    比如测试用例里就有个“+-2”）；
# 3. 字符串可以包含0~9以外的字符，如果遇到非数字字符，那么只取该字符之前的部分，
#    如“-00123a66”返回为“-123”；
# 4. 如果超出int的范围，返回边界值（2147483647或-2147483648）。

"""


class Solution:
    # @param {string} str
    # @return {integer}
   def myAtoi(self, str):       
        str = str.strip()
        newStr = []
        for i in xrange(len(str)):
            if '0' <= str[i] <= '9' or (str[i] in ('+', '-') and i == 0):
                newStr.append(str[i])
            else:
                break
        if newStr in ([], ['+'], ['-']):
            return 0
        elif -2147483648 <= int(''.join(newStr)) <= 2147483647:
            return int(''.join(newStr))
        elif int(''.join(newStr)) > 2147483647:
            return 2147483647
        else:
            return -2147483648


"""My own codes
    (str[i] in ('+','-') and i==0): 是为了解决“+-2” cases；不管有多少+-号， 只将第一个符合存入ans， 通过i==0实现
    ”-00123“ 通过int转化自动处理
"""
 def myAtoi(self, str):
        str = str.strip()
        ans = []
        y = 0
        # if str=="":return -1
        for i in range(len(str)):
            if '0'<= str[i] <= '9' or (str[i] in ('+','-') and i==0): # 不能用str[0] in '+-':
                ans += str[i]
            else:
                break
        if ans in ([],['+'],['-']):return 0  # 开始忘记了这个corner case
        if -(1<<31) < int(''.join(ans)) < (1<<31)-1:
            return int(''.join(ans))
        elif int(''.join(ans)) >=(1<<31)-1 :
            return (1<<31)-1
        else:
            return -(1<<31)




    	

if __name__ == '__main__':
	b = Solution()
	s = "12399+"
	print b.myAtoi(s)


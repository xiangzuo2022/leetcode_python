class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
    	num1 = num1[::-1]; num2 = num2[::-1]
    	array = [0 for i in range(len(num1)+len(num2))]
    	for i in range(len(num1)):
    		for j in range(len(num2)):
    			array[i+j] += int(num1[i]) * int(num2[j])
    	ans = []
    	for i in range(len(array)):
    		digit = array[i] % 10
    		carry = array[i] / 10
    		if i < len(array)-1:
    			array[i+1]+= carry
    		ans.insert(0,str(digit))
    	while ans[0] == '0' and len(ans) > 1:
    		del ans[0]
    	return ''.join(ans)
if __name__ == '__main__':
	a = Solution()
	#  http://www.cnblogs.com/zuoyuan/p/3781515.html


"""
# ********* The Second Time *************
# 解题思路：两个非负数字字符串的相乘。其实就是大数乘法。算法的关键是要先将两个字符串翻转过来，然后按位进行
# 相乘，相乘后的数不要着急进位，而是存储在一个数组里面，然后将数组中的数对10进行求余（%），就是这一位的数，
# 然后除以10，即/10，就是进位的数。注意最后要将相乘后的字符串前面的0去掉.
"""

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        num1 = num1[::-1]; num2 = num2[::-1] # 逆序后方便后面的操作
        tmp = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                tmp[i+j] += int(num1[i]) * int(num2[j]) # 如果i+j的值相同则叠加， 这个和手算是一样的逻辑
        ans = []
        for i in range(len(tmp)):
            digit = tmp[i] % 10
            carry = tmp[i] / 10
            if i < len(tmp)-1:  # 下面是i+1， 所以i不能取到len(tmp)-1
                tmp[i+1] += carry  # 不是当前位接受进位是后面一位因为reverse了
            ans.insert(0,str(digit)) # 前面逆序了， 所以这里总是在首部插入,其实就是再reverse回来
        while ans[0]=='0' and len(ans) > 1: # 前面可以有多个0， 所以用while
            del ans[0]
        return ''.join(ans)




        























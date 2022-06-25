"""
先转换为十进制做加法然后再转换回二进制
"""
class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
    	a = int(a,2)
    	b = int(b,2)
    	return bin(a+b)[2:]  # 0b means binary so we need to read from the 3rd one



  # ************ The Second Time ***************
  """
  想想十进制是如何转二进制的， 就是除以2得余数 %
  二进制数相加，并且保存在string中，要注意的是如何将string和int之间互相转换，并且每位相加时，会有进位的可能，
  会影响之后相加的结果。而且两个输入string的长度也可能会不同。这时我们需要新建一个string，它的长度是两条输入string中的较大的那个，
  并且把较短的那个输入string通过在开头加字符‘0’来补的较大的那个长度。这时候我们逐个从两个string的末尾开始取出字符，然后转为数字，
  想加，如果大于等于2，则标记进位标志carry，并且给新string加入一个字符‘0’
  """
  class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        solution = []
        sum = 0
        for i in range(0,max(len(a),len(b))):
            if i < len(a) and a[len(a)-1-i]=='1':
                sum += 1
            if i < len(b) and b[len(b)-1-i]=='1':
                sum += 1
            solution.insert(0,str(sum%2))  # % 后往前插
            sum /= 2
        if sum > 0:
            solution.insert(0,str(sum%2))
        return ''.join(solution)




















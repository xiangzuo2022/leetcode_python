class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
    	stack  = [] 
        for i in tokens:
            try:
                temp = int(i)
                stack.append(temp)
            except Exception, e:         
                b,a = stack[-1],stack[-2]
                stack.pop()
                stack.pop()
                if i == '+':    a = a+b
                elif i=='-':    a = a-b
                elif i=='*':    a = a*b
                elif i=='/':    a = int(a*1.0/b)
                stack.append(a)

        return stack[-1]


#  ********** The Second Time *************
"""
# 解题思路：这道题是经典的逆波兰式求值。具体思路是：开辟一个空栈，遇到数字压栈，遇到运算符弹出栈中的两
# 个数进行运算，并将运算结果压栈，最后栈中只剩下一个数时，就是所求结果。这里需要注意的一点是python中
# 的'/'除法和c语言不太一样。在python中，(-1)/2=-1，而在c语言中，(-1)/2=0。也就是c语言中，除法是向
# 零取整，即舍弃小数点后的数。而在python中，是向下取整的。而这道题的oj是默认的c语言中的语法，所以需要
# 在遇到'/'的时候注意一下。
"""

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []
        for i in range(0,len(tokens)):
            if tokens[i]!='+' and tokens[i]!='-'and tokens[i]!='*'and tokens[i]!='/':
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '+':
                    stack.append(a+b)
                if tokens[i] == '-':
                    stack.append(a-b)
                if tokens[i] == '*':
                    stack.append(a*b)
                if tokens[i] == '/':
                    if a*b < 0:
                        stack.append(-((-b)/a))
                    else:
                        stack.append(b/a)
        return stack.pop()



"""
My own codes: the idea is the same as above
"""
class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []        
        for i in range(len(tokens)):         
            if tokens[i] not in '+-*/':
                stack.append(int(tokens[i]))                
            else:               
                b = stack.pop();a = stack.pop()
                stack.append(self.compute(a,b,tokens[i]))
        return stack.pop()                
                
    def compute(self,a,b,op):   # 注意操作数的方向， - and / 需要考虑方向
        a = int(a); b = int(b)        
        if op == '+': return a+b
        if op == '-': return a-b
        if op == '*': return a*b
        if op == '/' and b != 0: # 漏掉了负数的case
            if a*b < 0:
                return -((-a)/b)
            else:
                return a/b

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        n = len(tokens)
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a+b)
                if token == '-':
                    stack.append(a-b)
                if token == '*':
                    stack.append(a*b)
                if token == '/' and b!=0:
                    if a*b < 0:
                        stack.append(-((-a)/b)) 
                    else:
                        stack.append(a/b)
                    
        return stack.pop()























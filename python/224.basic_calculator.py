class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):        
        operands, operators = [], []
        operand = ""
        for i in reversed(xrange(len(s))): # 从后向前
            if s[i].isdigit():
                operand += s[i]
                if i == 0  or not s[i-1].isdigit():
                    operands.append(int(operand[::-1]))
                    operand = ""
            elif s[i] == ')' or s[i] == '+' or s[i] == '-':
                operators.append(s[i])
            elif s[i] == '(':
                while operators[-1] != ')':
                    self.compute(operands, operators)
                operators.pop()
                
        while operators:
            self.compute(operands, operators)
            
        return operands[-1] # operands[0]

    def compute(self, operands, operators):
        left, right = operands.pop(), operands.pop()
        op = operators.pop()
        if op == '+':
            operands.append(left + right)
        elif op == '-':
            operands.append(left - right)


"""
将数字和操作符分开记录,此题没有优先级较为简单
从后向前处理会比较容易些
没弄明白为什么从前往后不能通过所有test cases, 只能通过部分
"""
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        number,oper = [],[]
        tmp = ""  #数字可以是多于一位的；如果当前字符c是数字字符，数字可能不止一位，所以需要继续遍历下一个字符，若仍然是数字字符，将其与前面的连续数字字符组成一个数num，直到遇到下一个非数字字符；
        for i in reversed(range(len(s))):  # 从后向前
            if s[i].isdigit():
                tmp += s[i]
                if i == 0 or not s[i-1].isdigit():
                    number.append(int(tmp[::-1])) 数字在number中是正向的
                    tmp = ""
            elif s[i] ==')' or s[i] == '+' or s[i]=='-':
                oper.append(s[i])
            elif s[i] == '(':
                while oper[-1]!=')':
                    self.compute(number,oper)
                oper.pop()
        while oper:
            self.compute(number,oper)
        return number[0]


    def compute(self,number,oper):
        a,b = number.pop(),number.pop()
        op = oper.pop()
        if op == '+':
            number.append(a+b)
        if op == '-':
            number.append(a-b)



"""
discussion里面别人给我改后的
"""

class Solution:
    def calculate(self, s):
    
        num, op=[],[]
        n=len(s)
        tmp=""
        for i in range(n):
            if s[i].isdigit():
                tmp+=s[i]
                if i==n-1 or not s[i+1].isdigit():
                    num.append(int(tmp))
                    tmp=""
            elif s[i] in "(+-":
                op.append(s[i])
            elif s[i]==")":
                while op[-1]!="(":
                    self.compute(num,op)
                op.pop()

        while op:
            self.compute(num, op)

        return num[-1]
        
    def compute(self, num, op):
        a, b=num.pop(), num.pop()
        l=len(op)
        asign=op.pop()
        if l==1 or op[-1]=="(":
            if asign=="+":
                num.append(a+b)
            elif asign=="-":
                num.append(b-a)
            return

        bsign= op.pop()
        if asign == bsign:
            num.append(a+b)
            op.append(asign)
        elif asign!=bsign:
            if a > b:
                num.append(a-b)
                op.append(asign)
            elif b > a:
                num.append(b-a)
                op.append(bsign)








if __name__ == '__main__':
    a = Solution()
    print a.calculate("1+1")


    			


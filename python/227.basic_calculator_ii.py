"""
直接使用eval可以过。。然后算法的话，使用下下面的方法：

用num保存上一个数字，用pre_op保存上一个操作符。当遇到新的操作符的时候，需要根据pre_op进行操作。乘除的优先级高于加减。所以有以下规则：

之前的运算符是+，那么需要把之前的数字num进栈，然后等待下一个操作数的到来。 
之前的运算符是-，那么需要把之前的数字求反-num进栈，然后等待下一个操作数的到来。 
之前的运算符是×，那么需要立刻出栈和之前的数字相乘，重新进栈，然后等待下一个操作数的到来。 
之前的运算符是/，那么需要立刻出栈和之前的数字相除，重新进栈，然后等待下一个操作数的到来。

注意比较的都是之前的操作符和操作数，现在遇到的操作符是没有什么用的。

另外，坑爹的Python地板除。。比如-3//2=2的，和c++不一样。因此真正操作的时候如果遇到负数，使用的用浮点除再取整的方式获得和c++一样的结果。
"""

class Solution(object):
    def calculate(self, s)
        """
        :type s: str
        :rtype: int
        """
        if not s: return "0"
        stack, num, sign = [], 0, "+"
        for i in xrange(len(s)):
            if s[i].isdigit():
                num = num*10+ord(s[i])-ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp % num != 0:  # remember this 
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = s[i]
                num = 0
        return sum(stack)
      
      
"""
offical solution
"""
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        preSign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0') # convert string to integer, the integer could be 102
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                preSign = s[i]
                num = 0
        return sum(stack)
      
"""
python 2 code
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        stack = []
        preSign = '+'
        num = 0
        for i in range(n):
            if  s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0') # convert string to integer, the integer could be 102
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp % num != 0:  # remember this 
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                preSign = s[i]
                num = 0
        return sum(stack)

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-ii-by-leetcode-solutio-cm28/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
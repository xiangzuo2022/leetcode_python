"""
思路和算法

保证左右括号数量的 平衡： 计算 '(' 出现的次数减去 ')' 出现的次数。如果值为 0，那就是平衡的，如果小于 0，就要在前面补上缺少的 '('。

计算 S 每个前缀子数组的 平衡度。如果值是负数（比如说，-1），那就得在前面加上一个 '('。同样的，如果值是正数（比如说，+B），那就得在末尾处加上 B 个 ')' 。

"""

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = 0
        for symbol in s:
            if symbol == '(':
                right += 1
            else:
                right -=1  
            # It is guaranteed right >= -1
            if right == -1:
                left += 1
                right += 1 # reset right to 0
        return left + right

"""
use stack
"""
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if not stack or (stack and stack[-1]==')'):
                    stack.append(s[i])
                else:
                    stack.pop()
                    
        return len(stack)
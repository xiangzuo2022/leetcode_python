class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curnum = 0
        curstring = ''
        stack = []
        for char in s:
            if char == '[':
                stack.append(curstring)
                stack.append(curnum)
                curstring = '' # clear them every time
                curnum = 0
            elif char == ']':
                prenum = stack.pop()
                prestring = stack.pop()
                curstring = prestring + prenum * curstring
            elif char.isdigit():  # e.g., 100
                curnum = curnum * 10 + int(char)
            else:  # chars
                curstring += char
        return curstring
      
"""
Solution 2
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, res, curnum = [], "", 0
        for char in s:
            if char == '[':
                stack.append([curnum, res])
                res, curnum = "", 0
            elif char == ']':
                num, last_res = stack.pop()
                res = last_res + num * res
                print(last_res, num, num*res, res)
            elif '0' <= char <= '9':
                curnum = curnum * 10 + int(char)            
            else:
                res += char
        return res
    


# https://www.youtube.com/watch?v=qB0zZpBJlh8

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] !="[":    
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)
           
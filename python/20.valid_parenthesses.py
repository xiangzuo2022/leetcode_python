class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
    	paren_map = {
    	'(':')',
    	'{':'}',
    	'[':']'
    	}
    	stack = []
    	for p in s:
    		if p in paren_map:
    			stack.append(paren_map[p])
    		else:
    			if not stack or stack.pop()!=p:
    				return False
    	return not stack  # as stack is empty == False but we need to return True

# *************** The Second Time *****************
"""
# Solution: if ([{ push to the stack and )]} pop
解法很巧妙， 入占和比较的都是')'.
"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        d = {'(':')','[':']','{':'}'}  # smart using of a dictionary
        stack = []
        for e in s:
            if e in d:
                stack.append(d[e])
            elif not stack or stack.pop()!= e:
                return False
        return not stack

# ***************** The Third Time *********************
"""
My own soluiton:常规解法，成对就pop，代码繁琐
"""
class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if s == []: return False
        stack = []
        for i in range(len(s)):

            if stack == [] or s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            if s[i]==')' and stack[-1]=='(':
                stack.pop()
            elif s[i]==')' and stack[-1]!='(':
                stack.append(s[i])
            
            if s[i]==']' and stack[-1]=='[':
                stack.pop()
            elif s[i]==']' and stack[-1]!='[':
                stack.append(s[i])
            
            if s[i]=='}' and stack[-1]=='{':
                stack.pop()
            elif s[i]=='}' and stack[-1]!='{':
                stack.append(s[i])
            
         
        return len(stack) == 0   # or return not stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {')':'(', ']':'[', '}':'{'}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return stack == []
    
# https://www.youtube.com/watch?v=WTzjTskDFMg

"""
([)] this case does not work beause the order is not right; we can start with open brackets but not close brackets
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in closeToOpen:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return stack == []








        



























# 用一个栈记录左括号, 右括号和index, 如果当前括号是右括号且栈顶是左括号, 则弹栈并更新maxLen。
# 解题思路：返回括号串中合法括号串的长度。使用栈。这个解法比较巧妙，开辟一个栈，压栈的不是括号，
# 而是未匹配左括号的索引！
# 因为求长度所以stack里存index

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
    	#if not s: return 0
    	maxLen = 0; stack = [-1]
    	for i in range(len(s)): 
    		
    		if s[i] == ')' and s[stack[-1]]=='(' and stack[-1]!= -1:
    			stack.pop()
    			maxLen = max(maxLen,i - stack[-1]) 
    		else:
    			stack.append(i)   		
    	return maxLen

if __name__ == '__main__':
	a = Solution()
	print a.longestValidParentheses("()(()")

	    	

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
    	stack = []
    	res = ''
    	for i in range(len(path)):
    		end = i + 1
    		while end < len(path) and path[end] != '/':
    			end += 1
    		sub = path[i+1:end]
    		if len(sub) > 0:
    			if sub == '..':
    				if stack:
    					stack.pop()
    				elif sub != '.':
    					stack.append(sub)
    		i = end
    	if not stack:
    		return '/'
    	for i in stack:
    		res += '/' + i
    	return res
        
"""
# ******* The Second Time *********
# 解题思路：题目的要求是输出Unix下的最简路径，Unix文件的根目录为"/"，"."表示当前目录，".."表示上级目录。
# 使用一个栈来解决问题。遇到'..'弹栈，遇到'.'不操作，其他情况下压栈。
"""
class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        stack = ['/']
        for i in path.strip('/').split('/'):
            if i == '.' or i == '':continue
            if i == '..':
                if len(stack) > 1: # 为0 没有可pop的
                    stack.pop()
                else:
                    stack.append(i+'/')
        if len(stack) > 1:
            return ''.join(stack).rstrip('/') # 尾部移掉'/'
        else:
            return ''.join(stack)


# This method returns a copy of the string in which all chars have been stripped from the 
# end of the string (default whitespace characters).


#************ The Third Time *********************
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = ['/']
        for i in path.split('/'):
            if i == '.' or i =='':continue
            elif i == '..':
                if len(stack) > 1: # 为0 没有可pop的
                    stack.pop()
            else:
                stack.append(i+'/')
        if len(stack) > 1:
            return ''.join(stack).rstrip('/') # 尾部移掉'/'
        else:
            return ''.join(stack)





















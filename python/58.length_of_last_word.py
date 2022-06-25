# Solution 1:
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        res = []
        res = s.strip().split(' ')
        return len(res[-1])


# Solution 2:
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
    	if s == "": return 0
    	stack = []
    	if s[-1] == ' ':
    		s = s[:-2]
    	for i in range(len(s)-1,-1,-1):
    		if s[i] != ' ':
    			stack.append(s[i])
    		else:
    			break
    	return len(stack)

# my own solution, which is much shorter
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):    
        count = 0                  
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ': count+= 1
            elif s[i] == ' ' and count > 0: 
                return count
       	return count





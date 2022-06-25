# This method uses python's build-in method split(),which might not be accepted by intervew.
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
    	s_split = s.split()
    	if len(s_split) == 0:
    		return 0
    	else:
    		return len(s_split[-1])


# Solution 2: traverse the array from the end to the front
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
    	n = len(s)   	
    	count = 0    	
    	if n==0:
    		return 0
    	if n == 1:
    		if s[0] == ' ':
    			return 0
    		else:
    			return 1
    	for i in range(n-1,-1,-1):    		
    		if s[i] != ' ':    			
    			count += 1
    		elif s[i] == ' ' and count > 0:  # this condition is critical 
    			return count
    	return count







if __name__ == '__main__':
	a = Solution()
	print a .lengthOfLastWord('a ')
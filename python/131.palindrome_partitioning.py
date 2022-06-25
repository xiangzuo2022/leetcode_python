class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
    	Solution.res = []
    	self.dfs(s,[])
    	return Solution.res

    def isPalindrome(self,s):  #单个字符的判断回文
    	for i in range(len(s)):
    		if s[i] != s[len(s)-i-1]:
    			return False
    	return True


   	def dfs(self,s,stringlist):
   		if len(s)== 0: 
   			Solution.res.append(stringlist)
   		for i in range(1,len(s)+1):
   			if self.isPalindrome(s[:i]):
   				self.dfs(s[i:],stringlist+[s[:i]])



"""
我的更简洁的写法
"""
class Solution(object):
    def isPalindrome(self, s):        
        if s[:] == s[::-1]:return True
        return False
            
    def partition(self, s):
        def dfs(s, stringlist):
            if len(s) == 0: res.append(stringlist)
            for i in range(1, len(s)+1): 
                if self.isPalindrome(s[:i]):
                    dfs(s[i:], stringlist+[s[:i]])# 若从0开始这里s[:i]和s[i:]是一样的
        res = []
        dfs(s, [])
        return res
      
"""
another implementation 
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        path = []
        def isPalindrome(s):
            if s[:] == s[::-1]:
                return True
            else:
                return False
            
        def backtrack(s, startIndex):
            if startIndex >= len(s):
                return ans.append(path[:])
            for i in range(startIndex, len(s)):
                p = s[startIndex:i+1]
                if isPalindrome(p):
                    path.append(p)
                else:
                    continue
                backtrack(s, i+1)
                path.pop()
                
        backtrack(s, 0)
        return ans
        


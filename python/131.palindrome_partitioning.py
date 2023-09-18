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
    

# https://www.youtube.com/watch?v=3jvWodd7ht0&list=PLot-Xpze53lf5C3HSjCnyFghlW0G1HHXo&index=5
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return 
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        


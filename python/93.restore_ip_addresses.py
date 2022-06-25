class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
    	def dfs(s,sub,ips,ip):
    		if sub == 4:
    			if s == '':
    				ips.append(ip[1:])
    			return 
    		for i in range(1,4):
    			if i <= len(s):
    				if int(s[:i]) <= 255:
    					dfs(s[i:],sub+1,ips,ip+'.'+s[:i])
    				if s[0] == '0':
    					break
    	ips = []
    	dfs(s,0,ips,'')
    	return ips



# *******The Second Time *********
"""
典型DFS
# 递归。查找所有的ip格式。注意，ip格式为四位，每一位为0~255，所以每一位可能有1~3位数。
# 这道题目主要主要多种情况的判断：
# 结束标志为：cur == 4 && index == s.length() 即ip为四位，并且index下标刚好遍历完。
# ip地址每一位格式不能为0xx（01 001 都是不允许的）记得判断每一位ip都要小于等于255
"""



class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):        
        
        def dfs(s,sub,ip):
        
            if sub == 4:  #此处不能用sub == 4 and s=='', 因为只要sub==4就return不是要满足两个条件才return，否则time out
                if s == '':
                    ans.append(ip[1:])# 从1开始是因为第一个为'.'
                return
            
            for i in range(1,4):  # ip的每一段可能有1-3位数
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        dfs(s[i:],sub+1,ip+'.'+s[:i])
                    if s[0] == '0':
                        break

        ans = []
        dfs(s,0,'')
        return ans

"""
use backtrack template
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """  
  
        res = []
        path = []
    
        def backtrack(s, start):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return
            for i in range(start, min(start+3, len(s))):
                if s[start] == '0' and i > start:
                    continue
                if 0 <= int(s[start:i+1]) <= 255:
                    path.append(s[start:i+1])
                    backtrack(s,  i + 1)
                    path.pop()
        backtrack(s, 0)
        return res













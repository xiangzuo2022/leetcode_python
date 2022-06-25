class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):

    	a = version1.split('.')
    	b = version2.split('.') 
    	i = 0   	 # i is a global variable
    	while i < min(len(a),len(b)):    		
    		if int(a[i]) > int(b[i]):
    			return 1
    		elif int(a[i]) < int(b[i]):
    			return -1
    		i = i + 1
    	if len(a) > len(b) and sum([int(e) for e in a[i:]]) != 0:
    		return 1
    	elif len(a) < len(b) and sum([int(e) for e in b[i:]]) != 0:
    		return -1
    	else:
    		return 0


# ************ The Second Time *************
"""
# Solution: deal with corner cases, e.g., 01,1; different lengths 
# convert to int to compare!!!
"""
class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        a = version1.split('.')
        b = version2.split('.')
        len1 = len(a)
        len2 = len(b)
        lenMax = max(len1,len2)
        for i in range(lenMax):
            tmp1 = 0
            if i < len1:
                tmp1 = int(a[i])  # int can solve the 01 case
            tmp2 = 0
            if i < len2:
                tmp2 = int(b[i])
            if tmp1 < tmp2:
                return -1
            if tmp1 > tmp2:
                retun 1
        return 0

"""
以上思路的另一种写法:长度不够的用‘0’补， 这是关键！！！
"""
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        a = version1.split('.')
        b = version2.split('.')
        
        length = max(len(a),len(b))
        for i in range(length):
            
            if i < len(a):
                tmp1 = int(a[i])
            else:
                tmp1 = 0
            if i < len(b):
                tmp2 = int(b[i])
            else:
                tmp2 = 0
            if tmp1 < tmp2:return -1
            elif tmp1 > tmp2:
                return 1
        return 0
    		
    
    	
if __name__ == '__main__':
	a = Solution()
	print a.compareVersion('1','1.1')

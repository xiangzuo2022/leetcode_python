"""
alphanumeric characters是字母加数字的意思；字母的大写与小写相差32.
# 什么是回文: https://zh.wikipedia.org/wiki/%E5%9B%9E%E6%96%87%E6%95%B0
# 将整数翻转，之后比较，若跟原来的数相等，就是回文数字  
# 若1234321，倒转之后数字为1234321，相等，就是回文数字 
# 解题思路：将不是字母的字符去掉，然后转换成小写，然后简单的回文判断。
"""

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
    	
    	tmp = []
    	for i in s:
    		if 'a' <= i <= 'z' or '0' <= s[i] <= '9' :
    			tmp.append(i)    	
    		elif 'A' <= i <= 'Z':  # change all to lower case
    			tmp.append(chr(ord(i)-ord('A')+ord('a')))

    	return tmp[::] == tmp[::-1]



""" 
更简洁的写法
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = []
        for i in s:
            if '0' <= i <= '9' or 'a'<= i <= 'z':
                ans.append(i)
            elif 'A'<=i<='Z':
                i = i.lower()
                ans.append(i)
        return ans[:] == ans[::-1]


"""
Another method
"""class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        for e in s:
            if '0' <= e <= '9' or 'a' <= e.lower() <= 'z':
                res.append(e.lower())
        return res[::] == res[::-1]
      
"""
直接法
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]



"""
two pointers solution
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left, right = 0, n - 1
        
        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1
        return True

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/valid-palindrome/solution/yan-zheng-hui-wen-chuan-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
    	d = {}
    	if s==t:
    		return True
    	for i range(0,len(s)):
    		if s[i] not in d:
    			if t[i] not in d.values():
    				d[s[i]] = t[i]
    			else:
    				return False
    		elif t[i]!=d[s[i]]:
    			return False
    	return True




class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        d = {}
        if s==t:
            return True
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] not in d.values():
                    d[s[i]] = t[i]
                else:
                    return False
            elif t[i]!= d[s[i]]:
                return False
        return True


# Solution: element in s as key in a dictionary while element in t as the key's value.
# compare d[s[i]] with t[i], if equal then return True otherwise return False.
# one dictinoary is enought no need to use two. 
# 题目大意：
# 给定两个字符串s和t，判断它们是否是同构的。
# 如果字符串s可以通过字符替换的方式得到字符串t，则称s和t是同构的。
# 字符的每一次出现都必须被其对应字符所替换，同时还需要保证原始顺序不发生改变。两个字符不能映射到同一个字符，
# 但是字符可以映射到其本身。测试样例如题目描述。可以假设s和t等长。



        




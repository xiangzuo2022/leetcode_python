class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):

    	d = {}
    	res = []
    	for i in range(len(s)):
    		key = s[i:i+10]
    		if key not in d:
    			d[key] = 1
    		else:
    			d[key] += 1

    	for e in d:
    		if d[e] > 1:
    			res.append(e)

    	return res


#  ******* The Second Time *********
# 我的思路是对的， 但是细节处理不够好

class Solution:
    # @param {string} s
    # @return {string[]} 


    def findRepeatedDnaSequences(self, s):
        d = {}
        ans = []
        for i in range(len(s)):
            if i + 10 <= len(s):  # I think we need this judegment. This is from my own part.
                part2 = s[i:i+10]
                tmp =  part2
                if tmp not in d:
                    d[tmp] = 1
                else:
                    d[tmp]+=1
        for key in d:
            if d[key] > 1:
                ans.append(key)
        return ans


"""
The second programing way
"""
class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        d = {}; n = len(s);ans = []
        if n < 10:return ans
        for i in range(n):
            key = s[i:i+10]
            if key not in d:
                d[key] = 1
            else:
                d[key] += 1
                if key not in ans:
                    ans.append(key)
        return ans













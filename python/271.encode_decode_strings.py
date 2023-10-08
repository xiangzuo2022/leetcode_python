"""
用字符串的长度和结束字符来encode
"""
class Solution:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for e in strs:
            res += str(len(e)) + ':'+ e
        
        return res
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        ans = []
        i = 0
        while i < len(s):
            index = s.find(':',i) # substring search from i 
            
            size = int(s[i:index])  # get the length of current string 
            print(s[i:index])         
            ans.append(s[index+1:index+1+size])
            i = index+1+size
        
        return ans
    
# https://www.youtube.com/watch?v=B1k_sxOSgv8
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s            
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j + 1 + length
        return res
            
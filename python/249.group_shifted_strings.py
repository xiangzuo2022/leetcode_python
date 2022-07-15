"""
把每个string的根据ASCII码，每个字符减去第一个字符的ASCII码，从而产生一个从0开始的list，
这样，只要出现一个相同的list，那么就是可以被shift到的一个string。
a video explains https://www.youtube.com/watch?v=H4U37GnpjXo
归为一类的string的共同点是字符之间差值一样
"""

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strings:
            d = ord(s[0]) - ord('a')
            key = tuple((ord(ch) - d) % 26 for ch in s)
            if key not in dic:
                dic[key] = [s]
            else:
                dic[key] += [s]

        ans = []
        for key in dic:
            ans.append(dic[key])
        return ans


"""
my own solution
"""
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        ans = []
        for s in strings:
            d = ord(s[0]) - ord('a')
            temp = []
            for ch in s:
                temp.append((ord(ch) - d) % 26)           
            key = ','.join(str(a) for a in temp)
            
            if key not in dic:
                dic[key] = [s]
            else:
                dic[key] += [s]
                
        for key in dic:
            ans.append(dic[key])
        return ans
"""
# 解题思路：anagram的意思是：abc，bac，acb就是anagram。即同一段字符串的字母的不同排序。
# 将这些都找出来。这里使用了哈希表，即Python中的dict。针对前面的例子来讲，映射为{abc：abc，bac，acb}。
"""

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dict = {}
        for word in strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
        res = []
        for item in dict:
            if len(dict[item]) >= 2:
                res += dict[item]
        return res




# ******** The third time **********
#  最新的写法， test cases changed.
class Solution:
    # @param {string[]} strs
    # @return {string[]}
     def groupAnagrams(self, strs):
      d = {}
      ans = []
      for word in strs:
        s_word = ''.join(sorted(word))
        if s_word not in d:
          d[s_word] = [word]
        else:
          d[s_word] += [word]

      for key in d:
        if len(d[key]) > 1:
          ans += [d[key]]
        else:
          ans += [d[key]]
      return ans



"""
完全通过的解法
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
       
        d = dict(); ans = []
        for e in strs:
            ee = ''.join(sorted(e))
            if ee not in d:
                d[ee] = [e]
            else:
                d[ee]+= [e]
                
        for key in d:
            ans.append(sorted(d[key]))
        return ans

"""
A similar writing way
"""     

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = []
        d = {}
        n = len(strs)
        if n == 0:
            return ans
        for word in strs:
            key = ''.join(sorted(word))
            if key not in d:
                d[key] = [word]
            else:
                d[key] += [word]

        for key in d:
            ans += [d[key]]
        return ans

"""
official solution
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            d[key].append(str)
        return list(d.values())










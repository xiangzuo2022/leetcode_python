"""
use hashtable
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        n, m = ransomNote, magazine
        if m == 0:
            return False
        for letter in magazine:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1

        for r in ransomNote:
            if r in d and d[r] > 0:  # delete
                d[r] -= 1
            else:
                return False
        return True


"""
use set, count
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

"""
Python写法一（使用数组作为哈希表）：
用数组干啥，都用map完事了，其实在本题的情况下，使用map的空间消耗要比数组大一些的，因为map要维护红黑树或者哈希表，而且还要做哈希函数，
是费时的！数据量大的话就能体现出来差别了。 所以数组更加简单直接有效！
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26
        for x in magazine:
            arr[ord(x) - ord('a')] += 1

        for x in ransomNote:
            if arr[ord(x) - ord('a')] == 0:
                return False
            else:
                arr[ord(x) - ord('a')] -= 1        
        return True

"""
Python写法二（使用defaultdict）：
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        from collections import defaultdict

        hashmap = defaultdict(int)

        for x in magazine:
            hashmap[x] += 1

        for x in ransomNote:
            value = hashmap.get(x)
            if value is None or value == 0:
                return False
            else:
                hashmap[x] -= 1

        return True
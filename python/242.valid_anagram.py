"""
sort
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return s == t


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

"""
use two dictionaries
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        n = len(s)
        d = {}
        d2 = {}
        for letter in s:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1

        for l in t:
            if l not in d2:
                d2[l] = 1
            else:
                d2[l] += 1
        return d == d2


"""
use less space
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ans = [0] * 26
        for letter in s:
            pos = ord(letter) - ord('a')
            ans[pos] += 1

        for l in t:
            pos = ord(l) - ord('a')
            ans[pos] -= 1

        return ans == [0]*26
    
# https://www.youtube.com/watch?v=9UtInBqnCgA
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        countS = {}
        countT = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

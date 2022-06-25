"""
the same solution as 205
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern or not str:
            return False
        pattern = list(pattern)
        n = len(pattern)
        str = str.split(' ')
        d = {}
        if len(pattern) != len(str):
            return False
        for i in range(n):
            if pattern[i] not in d:
                if str[i] not in d.values():
                    d[pattern[i]] = str[i]
                else:
                    return False
            elif d[pattern[i]] != str[i]:
                return False
        return True

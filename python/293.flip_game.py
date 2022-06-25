"""
这道题让我们把相邻的两个++变成--，真不是一道难题，我们就从第二个字母开始遍历，
每次判断当前字母是否为+，和之前那个字母是否为+，如果都为加，
则将翻转后的字符串存入结果中即可
"""

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        ans = []
        for i in range(n-1):
            if s[i:i+2] == '++':
                ans.append(s[:i] + '--' + s[i+2:])
        return ans

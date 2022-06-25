"""
The main idea is two pointers. Initialization is an issue, either index1, index2 = n, n
or index1, index2 = -1, -1 plus a final check
"""


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(words)
        index1, index2 = -1, -1
        ans = n
        for i in range(n):
            if words[i] == word2:
                index1 = i
            if words[i] == word1:
                index2 = i
            if index1 != -1 and index2 != -1:
                ans = min(ans, abs(index1 - index2))
        return ans


    n = len(words)
        index1, index2 = n, n
        ans = n
        for i in range(n):
            if words[i] == word2:
                index1 = i
            if words[i] == word1:
                index2 = i
            ans = min(ans, abs(index1 - index2))
        return ans

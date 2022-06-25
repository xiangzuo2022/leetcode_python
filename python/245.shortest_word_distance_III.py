class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dic = {}     
        for index, value in enumerate(words):
            if value not in dic:
                dic[value] = [index]
            else:
                dic[value] += index,

        return min(set(abs(x-y) for x in dic[word1] for y in dic[word2]) - set([0]))

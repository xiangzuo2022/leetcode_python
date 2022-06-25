class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = {}
        self.n = len(words)
        for index, value in enumerate(words):
            self.d[value] = self.d.get(value,[]) + [index]
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = self.d[word1], self.d[word2]
        i = j = 0
        res = self.n
        # O(m+n) time complexity
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i]-l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res
        
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        d = [[0]() for i in range(m)]
        
        for i in range(1,m+1):
            d[0][i] = d[0][i-1] + 1
            
        for i in range(1,n+1):
            d[i][0] = d[i][0] + 1
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1])
        return d[m][n]
        
        
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)+1
        n = len(word2)+1
        d = [[0]*n for i in range(m)]
        
        for i in range(m):
            d[i][0] = i
            
        for j in range(n):
            d[0][j] = j
            
        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
        return d[-1][-1]
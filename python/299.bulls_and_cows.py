"""
思路一： 比较直观的想法是，按照A和B的定义，分别计算出它们的数目即可。注意在计算B时，要避免重复计数。
"""
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret = list(secret)
        guess = list(guess)
        A = B = 0

        i = 0
        while (i < len(secret)):
            if secret[i] == guess[i]:
                A += 1
                del secret[i]
                del guess[i]
            else:
                i += 1

        for c in secret:
            if c in guess:
                guess.remove(c)
                B += 1

        return str(A) + 'A' + str(B) + 'B'


"""
use dictionary
"""
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        d = {}
        bull, cow = 0,0

        for index,s in enumerate(secret):
            if guess[index] == s:
                bull += 1
            else:
                d[s] = d.get(s,0) + 1

        for index,s in enumerate(secret):
            if (guess[index] != s) & (d.get(guess[index],0) != 0):
        	    cow += 1
        	    d[guess[index]] -= 1
        	    
        return str(bull) + "A" + str(cow) + "B"

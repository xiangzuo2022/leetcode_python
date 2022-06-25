class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)
        res = 0
        flag = True
        
        for ch in text:
            if ch == ' ':
                if flag:
                    res += 1
                flag = True # reset the flag for next word
            elif ch in broken:
                flag = False
        if flag:
            res += 1
        return res
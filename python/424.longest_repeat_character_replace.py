# https://www.youtube.com/watch?v=gqXU1UyA8pk&t=13s
# slidng window + hashmap
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r - l + 1) - max(count.values()) > k: # this is the key: in this window minus the letter with highest frequency
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

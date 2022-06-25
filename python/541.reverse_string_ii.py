class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        t = list(s)
        def reverse(s):
            left, right = 0, len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return s
        
        for i in range(0, len(t), 2*k):
            t[i : i+k] = reverse(t[i:i+k])
        return "".join(t)
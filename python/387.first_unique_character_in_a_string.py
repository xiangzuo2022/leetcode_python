"""
use hashtable to record frequency 
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        if n == 0:
            return -1
        if n == 1:
            return 0
        d = {}
        for letter in s:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1

        for index, value in enumerate(s):
            if d[value] == 1:
                return index
        return -1
      
"""
use hashtable to record index and then in the second loop, only keys in the hashtable will be visited. Can save some time
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        position = dict()
        n = len(s)
        for i, ch in enumerate(s):
            if ch in position:
                position[ch] = -1
            else:
                position[ch] = i
        first = n
        for pos in position.values():
            if pos != -1 and pos < first:
                first = pos
        if first == n:
            first = -1
        return first

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string/solution/zi-fu-chuan-zhong-de-di-yi-ge-wei-yi-zi-x9rok/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


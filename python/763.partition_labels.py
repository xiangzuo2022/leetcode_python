"""
Greedy:图形解释非常好
https://zxi.mytechroad.com/blog/string/leetcode-763-partition-labels/
O(n)
"""
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_index = {}
        ans = []
        for i, val in enumerate(s):
            last_index[val] = i
            
        start = end = 0
        for i, val in enumerate(s):
            end = max(end, last_index[val])
            if i == end:
                ans.append(end - start + 1)
                start = end + 1
        return ans
      
      
"""
Another implementation
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = [0] * 26
        for i in range(len(s)):
            hash[ord(s[i]) - ord('a')] = i
        result = []
        left = 0
        right = 0
        for i in range(len(s)):
            right = max(right, hash[ord(s[i]) - ord('a')])
            if i == right:
                result.append(right - left + 1)
                left = i + 1
        return result
                
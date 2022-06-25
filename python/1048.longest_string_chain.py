"""
Explanation
Sort the words by word's length. (also can apply bucket sort)
For each word, loop on all possible previous word with 1 letter missing.
If we have seen this previous word, update the longest chain for the current word.
Finally return the longest word chain.


Complexity
Time O(NlogN) for sorting,
Time O(NSS) for the for loop, where the second S refers to the string generation and S <= 16.
Space O(NS)
"""
 def longestStrChain(self, words):
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in xrange(len(w)))
        return max(dp.values())
      
"""
"""
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dp = {}
        for w in sorted(words, key=len):
            best = 0
            for i in range(len(w)):
                prev = dp.get(w[:i] + w[i+1:], 0) 
                best = max(best, prev + 1)
            dp[w] = best  
        return max(dp.values())
        
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, dict):
    	dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]


# ********** The Second Time **********
"""
# DP
# 解题思路：这道题考察的显然不是dfs，为什么？因为这道题不需要给出如何分割的答案，只需要判断是否可以分割为
# 字典中的单词即可。我们考虑使用动态规划，这个思路看代码的话不难，用python写起来也比较清晰。
dp[i]=True 的含义是i以前到i的子串有一个在dict里就为True
"""


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]   

# https://www.youtube.com/watch?v=Sx9NNgInc3A&t=10s
# dp buttom up solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        # buttom up
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <=len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]

if __name__ == '__main__':
    a = Solution()
    print a.wordBreak("abcd", ["a","abc","b","cd"])


























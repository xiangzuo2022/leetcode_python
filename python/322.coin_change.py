class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        f = range(amount+1)
        n = len(coins)
        # initialization
        f[0] = 0
        for i in range(1,amount+1):
            f[i] = sys.maxint
            # f[i] = min{f[i-conins[0]]+1, f[i-coins[1]]+1,...f[i-conins[n-1]]+1}
            for j in range(n):
                if i >= coins[j] and f[i-coins[j]]!= sys.maxint:
                    f[i] = min(f[i-coins[j]]+1, f[i])
                
        if f[amount] == sys.maxint:
            f[amount] = -1
        return f[amount]
      
"""
完全背包，组合问题， 便利顺序两种都可以
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''版本一'''
        # 初始化
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        # 遍历物品
        for coin in coins:
            # 遍历背包
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1
    
    def coinChange1(self, coins: List[int], amount: int) -> int:
        '''版本二'''
        # 初始化
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        # 遍历物品
        for j in range(1, amount + 1):
            # 遍历背包
            for coin in coins:
                if j >= coin:
                	dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1
    

# https://www.youtube.com/watch?v=H9bfqozjoqs&t=14s
# DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount] != amount + 1 else -1
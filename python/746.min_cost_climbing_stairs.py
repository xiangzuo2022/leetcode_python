"""
A typical DP problem
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        #if n == 0: return 0
        #if n == 1: return cost[0]
        dp = [0 for i in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-2], dp[-1])
    
# https://www.youtube.com/watch?v=_i4Yxeh5ceQ&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=47
# bottom up DP
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)        

        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])

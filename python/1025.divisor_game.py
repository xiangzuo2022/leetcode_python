记dp[N]为黑板上数字为N的情况下,Alice的输赢情况， 如果Alice取了数字x, 那么显然
dp[N]与dp[N -x]输赢情况相反。x可以取的值很多，只要dp[N -xi]中任意一个为False, 那么dp[N]肯定为True, 否则dp[N]肯定为False

class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = {}
        dp[1] = False
        dp[2] = True
        for i in range(3, N + 1):
            dp[i] = False
            for j in range(1, i):
                if i % j == 0 and dp[i - j] == False:
                    dp[i] = True
                    break
        return dp[N]

作者：zhengkang
链接：https://leetcode-cn.com/problems/divisor-game/solution/fang-qi-shen-xian-jie-fa-hui-gui-pu-tong-ren-si-we/


class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        dp = [False] * (N+1)
        dp[1] = False
        if N >=2:
            dp[2] = True
        for i in range(3, N+1):
            for j in range(1, i):
                if i%j == 0 and dp[i-j] == False:
                    dp[i] = True
                    break
        return dp[N]
解题方案
思路：
标签：动态规划
首先初始化长度为n+1的数组dp，每个位置都为0
如果n为0，则结果为0
对数组进行遍历，下标为i，每次都将当前数字先更新为最大的结果，即dp[i]=i，比如i=4，最坏结果为4=1+1+1+1即为4个数字
动态转移方程为：dp[i] = MIN(dp[i], dp[i - j * j] + 1)，i表示当前数字，j*j表示平方数
时间复杂度：O(n*sqrt(n))，sqrt为平方根

class Solution:
    def numSquares(self, n: int) -> int:
        dp=[i for i in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,int(i**(0.5))+1):
                dp[i]=min(dp[i],dp[i-j*j]+1)
        return dp[-1]

链接：https://leetcode-cn.com/problems/perfect-squares/solution/dong-tai-gui-hua-bfs-zhu-xing-jie-shi-python3-by-2/

"""
首先，我们应该维护一个2维数组D，与地牢数组的大小相同，其中D[i][j]代表可以保证骑士在进入房间(i,j)之前，
探索其余地牢时能够存活下来的最小HP。显然D[0][0]就是我们随后需要的最终答案。因此，对于这个问题，我们需要从右
下角到左上角填充表格。
http://bookshadow.com/weblog/2015/01/07/leetcode-dungeon-game/
"""


class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
    	m = len(dungeon); n = len(dungeon[0])
    	dp = [[0] * n for i in range(m)]
    	dp[m-1][n-1] = max(0,-dungeon[m-1][n-1]) + 1
    	for i in range(m-1,-1,-1):
    		for j in range(n-1,-1,-1):
    			down = None
    			if i + 1 < m:
    				down = max(1,dp[i+1][j]-dungeon[i][j])
    			right = None
    			if j + 1 < n:
    				right = max(1,dp[i][j+1]-dungeon[i][j])
    			if down and right:
    				dp[i][j] = min(down,right)
    			elif down:
    				dp[i][j] = down
    			elif right:
    				dp[i][j] = right
    	return dp[0][0]

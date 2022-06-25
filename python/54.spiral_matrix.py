"""
# 一直向某个方向走，走到不能走顺时针旋转90度继续走
# 使用0,1,2,3四个值表示方向以便切换, 用maxUp, maxDown, maxLeft, maxRight四个变量记录四个边界。
# 当maxUp > maxDown 或 maxLeft > maxRight时就结束。
"""
class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
    	if len(matrix) == 0: return []
    	ans = []; down = len(matrix)-1; right = len(matrix[0])-1
    	left = up = 0
    	direct = 0
    	while True:
    		if direct == 0:  # go right
    			for i in range(left,right+1):
    				ans.append(matrix[up][i])
    			up += 1 # 从影响到索引的值去考虑就很容易理解：当走到最右边时up=0已被访问， 下次up从1开始
    		if direct == 1:  # go down
    			for i in range(up,down+1):
    				ans.append(matrix[i][right])
    			right -= 1
    		if direct == 2: # go left
    			for i in range(right,left-1,-1):
    				ans.append(matrix[down][i])
    			down -= 1
    		if direct == 3:  # go up
    			for i in range(down,up-1,-1):
    				ans.append(matrix[i][left])
    			left += 1
    		if up > down or left > right:
    			return res
    		direct = (direct + 1) % 4


# 在一个数组里移动的时候横坐标不变， 在不同数组里移动时纵坐标不变。





    	
    	
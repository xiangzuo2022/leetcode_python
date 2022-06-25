# 对于这个矩阵，对于每一行，我们按照上一道题的算法求解一遍，最后得出的就是最大的矩阵。
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
    	if matrix == []: return 0
    	maxArea = 0; m = len(matrix); n = len(matrix[0])
    	a = [0 for i in range(n)]
    	for i in range(m):
    		for j in range(len(matrix[i])):
    			if matrix[i][j] == '1':
    				a[j] = a[j] + 1   # a[j]里存的相当于84题里的高度
    			else:
    				a[j] = 0   
    		maxArea = max(maxArea,self.largestRectangleArea(a))
    	return maxArea
    	

    def largestRectangleArea(self, height):
        stack = []
        i = 0
        maxArea = 0
        h = height + [0]
        h_length = len(h)
        while i < h_length:
            # not stack means stack is empty
            if (not stack) or h[stack[-1]] <= h[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                maxArea = max(maxArea, h[t] * (i if not stack else i - stack[-1] - 1))
        return maxArea


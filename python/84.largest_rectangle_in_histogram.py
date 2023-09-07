"""
jiuzhang视频讲解的非常好, 一下是思路
# O(N)解法。要一个栈来存放非递减的height序列, 即碰到大于等于栈顶的就入栈, 碰到小于栈顶的就
# pop。对于每个pop出的元素h[stack[top]]，都要计算以它为最低高度的矩形的面积, 高度就是h[stack[top]], 
# 宽度就是i － stack[-1] - 1, 注意栈中的元素都是非递减的。在h末尾多加一个0的目的是保证栈中的元素都可
# 以被pop出。
"""

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        stack = []
        i = 0
        maxArea = 0
        h = height + [0]
        h_length = len(h)
        while i < h_length: # cannot use for loop    
            if (not stack) or h[stack[-1]] <= h[i]:
                stack.append(i)  # push index not value
                i += 1
            else:
                t = stack.pop()
                maxArea = max(maxArea, h[t] * (i if not stack else i - stack[-1] - 1))
        return maxArea

# 更详细的解释： http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html

# https://www.youtube.com/watch?v=zx5Sw9130L0
# mononic stack O(n) time complexity
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                 index, height = stack.pop()
                 maxArea = max(maxArea, height * (i - index))
                 start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))   
        return maxArea     

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
    	left = 0; right = len(height) -1 
    	area = 0
    	while left < right:
    		water = min(height[left],height[right]) * (right - left)
    		if water > area:
    			area = water
    		if height[left] < height[right]:
    			left += 1
    		else:
    			rihgt -= 1
    	return area



"""
# 解题思路：两个隔板的矮的那一个的高度乘以两个隔板的间距就是储水量
# 题目说的有点复杂，大意是利用x轴作底，两个任意的竖直线段作杯壁，何时盛水最多。
# 木桶原理大家肯定都知道，水盛多少取决于最短的杯壁，所以此题还可以引申为往围成的区域内放矩形，
# 怎样使得矩形面积最大。题目中的不能倾斜（slant：倾斜，倾倒）对应为矩形必须水平放置。
# 复杂度为O（n）的思想是贪心原理，先从底边最大的情况考虑，计算最大面积后，此时要将底边长度减1，
# 只需要将杯壁较短的那一边移动一个单位距离，得到的解必定优于杯壁较长那边移动的情况。
# 这样保证每次移动都得到的是局部最优解。
# 注意x的坐标是逐一增加的
"""

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        left = 0; right = len(height)-1
        ans = 0
        while left < right:
            water = (right-left) * min(height[left],height[right])
            if water > ans:
                ans = water
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


"""
My own codes: 两个指针; 贪心算法的典型
"""
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        p1 = 0; p2 = len(height)-1
        maxArea = 0
        while p1 < p2:
            maxArea = max(maxArea,abs(p2-p1)*min(height[p1],height[p2]))
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return maxArea
    

# soluction given by chatgpt
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        maxWater = 0
        while left < right:
            h_left = height[left]
            h_right = height[right]
            width = right - left
            min_h = min(h_left, h_right)
            maxWater = max(maxWater, width * min_h)

            if h_left < h_right:
                left += 1
            else:
                right -= 1
        return maxWater









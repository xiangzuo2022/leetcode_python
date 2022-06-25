class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        sums = (C-A)*(D-B) + (G-E)*(H-F)
        return sums - max(min(C,G)-max(A,E),0)*max(min(D,H)-max(B,F),0)


# 题目大意：
# 计算二维平面上两个直线矩形的覆盖面积。求出两个区域的面积, 然后减去overlapping的区域, 即为所求. 
# 矩形通过其左下角和右上角的坐标进行定义。
# 假设总面积不会超过int的最大值。
# 解题思路：
# 简单计算几何。根据容斥原理：S(M ∪ N) = S(M) + S(N) - S(M ∩ N)
# 题目可以转化为计算矩形相交部分的面积
# S(M) = (C - A) * (D - B)
# S(N) = (G - E) * (H - F)
# S(M ∩ N) = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
# 画个图一目了然， 谁减谁


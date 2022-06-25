class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        def check(x):
            rotation_a = rotation_b = 0            
            for i in range(n):
                if A[i] != x and B[i] != x:
                    return -1
                elif A[i] != x:
                    rotation_a += 1
                elif B[i] != x:
                    rotation_b += 1
            return min(rotation_a, rotation_b)
        
        n = len(A)
        rotation = check(A[0])
        if rotation != -1 :
            return rotation
        else:
            return check(B[0])


复杂度分析

时间复杂度：O(N)O(N)。我们只会遍历所有的数组最多两次。

空间复杂度：O(1)O(1)。

solution:
https://leetcode-cn.com/problems/minimum-domino-rotations-for-equal-row/solution/lian-xu-chai-xiang-tong-de-shu-zi-by-leetcode/
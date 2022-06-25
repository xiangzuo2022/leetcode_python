"""
2、验证法：题目说明最多有一个celebrity。利用这个信息，我们可以将算法的时间复杂度降低到O(n)：我们首先假定k号是celebrity，
然后依次判断i号是否认识k，一旦发现不认识，则说明k号不可能是candidate，而i号则有可能是candidate。
"""

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = 0
        for i in range(n):
            if (knows(k, i)):
                k = i
        for i in range(n):
            if (i != k and (knows(k, i) == True or knows(i, k) == False)):
                return -1

        return k

"""
graph是以邻接矩阵的形式给出的
"""
 
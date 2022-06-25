"""
解题思路：这道题要求两个已经排好序的数列的中位数。中位数的定义：如果数列有偶数个数，那么中位数为中间两个数的平均
值；如果数列有奇数个数，那么中位数为中间的那个数。比如{1，2，3，4，5}的中位数为3。{1，2，3，4，5，6}的中位数
为（3+4）/ 2 = 3.5。那么这题最直接的思路就是将两个数列合并在一起，然后排序，然后找到中位数就行了。可是这样最
快也要O((m+n)log(m+n))的时间复杂度，而题目要求O(log(m+n))的时间复杂度。这道题其实考察的是二分查找，
是《算法导论》的一道课后习题，难度还是比较大的。

首先转成求A和B数组中第k小的数的问题, 然后用k/2在A和B中分别找。比如k = 6, 分别看A和B中的第3个数, 
已知 A1 < A2 < A3 < A4 < A5... 和 B1 < B2 < B3 < B4 < B5..., 如果A3 <＝ B3, 那么第6小的数肯
定不会是A1, A2, A3, 因为最多有两个数小于A1, 三个数小于A2, 四个数小于A3。B3至少大于5个数, 所以第6小的数
有可能是B1 (A1 < A2 < A3 < A4 < A5 < B1), 有可能是B2 (A1 < A2 < A3 < B1 < A4 < B2), 有可能是
B3 (A1 < A2 < A3 < B1 < B2 < B3)。那就可以排除掉A1, A2, A3, 转成求A4, A5, ... B1, B2, B3, ...
这些数中第3小的数的问题, k就被减半了。每次都假设A的元素个数少, pa = min(k/2, lenA)的结果可能导
致k == 1或A空, 这两种情况都是终止条件。

"""

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
    	m = len(nums1); n = len(nums2)
    	t = (m+n)/2
    	if (m+n) % 2 == 1: # 奇数个
    		return self.getMedian(nums1, nums2, (m+n)/2 + 1)
    	else:
    		return 0.5*(self.getMedian(nums1,nums2,t) + self.getMedian(nums1,nums2,t+1))



    def getMedian(self, A, B, k):  # 寻找两个排序数组的第k小的数
    	m = len(A); n = len(B)
    	if m > n: return self.getMedian(B,A,k)  # by default A is larger than B
    	if m == 0: return B[k-1] # 直接返回B的中位数
    	if k == 1: return min(A[0],B[0])  #  第一个数是两个数组的最小数
    	pa = min(k/2,m); pb = k - pa
    	if A[pa-1] <= B[pb-1]:
    		return self.getMedian(A[pa:],B,k-pa) 
    	else:
    		return self.getMedian(A,B[pb:],k-pb)


"""
A more clear code
"""
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenA = len(A)
        lenB = len(B)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(A, B, (lenA + lenB)/2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB)/2) + self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5

    def getKth(self, A, B, k):
        lenA = len(A)
        lenB = len(B)
        if lenA > lenB:  # 保证A比B短
            return self.getKth(B, A, k)
        if lenA == 0:  # A已为空，直接返回B中间数
            return B[k - 1]
        if k == 1:   # 如果找的是第一个，直接返回两个数组比较小的那个
            return min(A[0], B[0])

        pa = min(k/2, lenA)
        pb = k - pa

        # 索引为pa和pb，所以是A[pa - 1] 和 B[pb - 1]
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)


"""
O(log(m+n)), jiuzhang solution 
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n%2:
            return self.findMedian(nums1,nums2,n/2+1)
        else:
            small = self.findMedian(nums1,nums2,n/2)
            big = self.findMedian(nums1,nums2,n/2+1)
            return (small + big) / 2.0
        
    def findMedian(self,A,B,k):
        if len(A) == 0:return B[k-1]
        if len(B) == 0: return A[k-1]
        if k == 1:
            return min(A[0],B[0])
        a, b = None, None
        if len(A) >= k/2:
            a = A[k/2-1]
        if len(B) >= k/2:
            b = B[k/2-1]
        if b is None or (a is not None and a < b):
            return self.findMedian(A[k/2:],B,k-k/2)
        return self.findMedian(A,B[k/2:],k-k/2)
            
        
        
        








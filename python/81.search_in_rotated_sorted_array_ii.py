"""
这道是之前那道 Search in Rotated Sorted Array 在旋转有序数组中搜索 的延伸，现在数组中允许出现重复数字，这个也会影响我们选择哪半边继续搜索，
由于之前那道题不存在相同值，我们在比较中间值和最右值时就完全符合之前所说的规律：如果中间的数小于最右边的数，则右半段是有序的，
若中间数大于最右边数，则左半段是有序的。而如果可以有重复值，就会出现来面两种情况，[3 1 1] 和 [1 1 3 1]，对于这两种情况中间值等于最右值时，
目标值3既可以在左边又可以在右边，那怎么办么，对于这种情况其实处理非常简单，只要把最右值向左一位即可继续循环，如果还相同则继续移，
直到移到不同值为止，然后其他部分还采用 Search in Rotated Sorted Array 在旋转有序数组中搜索 中的方法
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, A, target):
        left=0; right=len(A)-1
        while left<=right:
            mid=(left+right)/2
            if A[mid]==target: return True
            if A[left]==A[mid]==A[right]:  # 相等时左右同时移动指针
                left+=1; right-=1
            elif A[left]<=A[mid]:
                if A[left]<=target<A[mid]: right=mid-1
                else: left=mid+1
            else:
                if A[mid]<=target<A[left]: left=mid+1
                else:right=mid-1
        return False


        
"""
用二分法模板的方法: O(nlogn) is too large, not fast enough
此题无法优化到O(n)
// it ends up the same as sequential search
// We used linear search for this question just to indicate that the 
// time complexity of this question is O(n) regardless of binary search is applied or not.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:return False
        nums.sort()
        start = 0; end = len(nums)-1
        while start + 1 < end:
            m = (start + end)/2
            if nums[m]==target:return True
            if nums[start] < nums[m]:
                if nums[start] <= target and target <= nums[m]:
                    end = m
                else:
                    start = m
            else:
                if nums[m] <= target and target <= nums[end]:
                    start = m
                else:
                    end = m
        if nums[start] ==  target:
            return True
        if nums[end] == target:
            return True
        return False


"""
最直白的解法， 九章给出的 O(n)
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:return False
        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False



        
















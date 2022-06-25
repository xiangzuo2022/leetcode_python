  def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        begin, end = -1, -1
        n = len(nums)
        left = 0; right = n-1
        while left <= right:
            m = (left+right)/2
            if nums[m] > target:
                right = m-1
            elif nums[m] < target:
                left = m+1
            else:
                if nums[left] == target: begin = left
                if nums[right] == target: end = right
                for i in range(m, right+1):
                    if nums[i] != target:
                        end = i-1
                        break
                for i in range(m, left-1, -1):
                    if nums[i] != target:
                        begin = i + 1
                        break
                return [begin, end]
                
        return [-1,-1]


"""
用两次binary search, 同样使用二分法，先找到左端点，然后继续使用二分法去探查右端点。其中，在探查右端点的时候，
要以左端点为low。
很难control边界条件
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]

        low, high = 0, len(nums)-1
        while low < high:  # 查找左端点
            mid = (low+high)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        if nums[low] != target:  # 如果没有找到
            return [-1, -1]

        left = low
        high = len(nums) - 1
        while low < high:  # 继续二分查找 找 右端点
            mid = (low+high)//2 + 1
            if nums[mid] == target:
                low = mid
            else:
                high = mid - 1
        right = low
        return [left, right]
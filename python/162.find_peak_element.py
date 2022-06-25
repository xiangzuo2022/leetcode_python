"""
比较好理解的solution
"""
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1    
        while left < right-1:
            mid = (left+right)/2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
            
    
        return left if nums[left] >= nums[right] else right

"""
# Binary search O(nlogn)
# 思路：如果中间元素大于其相邻后续元素，则中间元素左侧(包含该中间元素）必包含一个局部最大值。
# 如果中间元素小于其相邻后续元素，则中间元素右侧必包含一个局部最大值。
"""
class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
    	return self.search(nums,0,len(nums)-1)

    def search(self,nums,start,end):
    	if start == end:
    		return start
    	if start + 1 == end:
            return [start, end][nums[start] < nums[end]]  
    	mid = (start + end)/2
    	if nums[mid] < nums[mid-1]:
    		return self.search(nums,start,mid-1)
    	if nums[mid] < nums[mid+1]:
    		return self.search(nums,mid+1,end)
    	return mid

"""
# ******* The Second Time **************
# O(n): 本题的一个重要特点是，从第一个元素开始，若其大于相邻的后续元素，则第一个元素就是一个局部最大值，
# 返回即可。若其小于相邻的后续元素，则第二个元素大于第一个元素。如此，一一遍历数组，第一次出现，
# 第i个元素若大于其相邻后续元素，则该元素就是一个局部最大值，返回即可
# 题意是只要后面比前面大即可
"""
class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):

        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                return i-1 
        return len(nums) -1 #其它情况return数组本生

"""
我自己的很蠢的方法， 但一次性通过
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return None
        if len(nums) == 1:return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i   
        
        
       
"""
九章二分法模板: O(n) 不是最优解法，O(logn)是更优的解法
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0; right = len(nums)-1
        while left + 1 < right:
            m = (left+right)/2
            if nums[m] < nums[m-1]:
                right = m
            elif nums[m] < nums[m+1]:
                left = m
            else:
                right = m
        if nums[left] < nums[right]:
            return right
        else:
            return left

"""
 用九章模板我自己写的，理解后发现很有意思;九章的模板很给力！！
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0; right = len(nums)-1
        while left + 1 < right:
            m = (left+right)/2
            if nums[m] < nums[m-1]:
                right = m
            elif nums[m] < nums[m+1]:
                left = m
            else: # m 大于m-1和m+1,上面的cases都是m不是peak值得情况
                return m
        if nums[left] < nums[right]: # 就剩两个元素的情况单独讨论
            return right
        else:
            return left


"""
my own solution, one-time pass
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return None
        n = len(nums)
        left = 0; right = n-1
        while left + 1 < right:
            m = (left+right)/2
            if nums[m] <= nums[m-1]:
                right = m
            elif nums[m] > nums[m-1]:
                left = m
        if nums[left] > nums[right]:
            return left
        else:
            return right
     
"""
official solution O(logn)
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # 辅助函数，输入下标 i，返回 nums[i] 的值
        # 方便处理 nums[-1] 以及 nums[n] 的边界情况
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]
        
        left, right, ans = 0, n - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid
                break
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        
        return ans

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/find-peak-element/solution/xun-zhao-feng-zhi-by-leetcode-solution-96sj/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。       
            
"""
another binary search implementation
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while low < high:
            mid = low + int((high-low)/2)
            if nums[mid] < nums[mid+1]:
                low = mid+1
            else:
                high = mid
        return low
      
"""
a more clear code
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums)-1
        while low < high:
            mid = low + int((high-low)/2)
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] < nums[mid+1]:
                low = mid+1
            else:
                high = mid-1
        return low if nums[low] >= nums[high] else high
            

if __name__ == '__main__':
    a = Solution()
    print a.findPeakElement([3,2,1])



























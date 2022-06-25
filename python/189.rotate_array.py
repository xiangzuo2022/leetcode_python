class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):

    	length = len(nums)
    	nums[:] = nums[length-k:length] + nums[0:length-k]
    	return nums

        # k可以比length大
    	nums[:] = nums[length - k % length : length] + nums[0 : length - k % length]


 """
 Solution 2
 """
 class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        n = len(nums)
        if n > 1 and k > 0:
            nums[:] = nums[n-k:] + nums[:n-k]

    # 必须是n-k, 不能是k+1, 因为 k+1可以超过数组范围 ！！！！


"""
solution 3
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            nums.insert(0,nums.pop())
            k -= 1

"""
九章反转三部曲
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:return
        k = k % len(nums)  # k可以大于n 
        n = len(nums)
    
        self.reverse(nums,0,n-1-k)
        print nums
        self.reverse(nums,n-k,n-1)
        print nums
        self.reverse(nums,0,n-1)
        print nums
        
    def reverse(self,s,begin,end):
        while begin < end:
            s[begin],s[end] = s[end],s[begin]
            begin += 1
            end -= 1
        

    	
if __name__ == '__main__':
 	a = Solution()
 	array = [1]
 	print a.rotate(array,0)

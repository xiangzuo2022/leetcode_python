"""
但是上面的解法不是O(1)的空间复杂度，所以我们需要另想一种解法，既然不能建立新的数组，那么我们只能覆盖原有数组，我们的思路是把1放在数组第一个位置nums[0]，
2放在第二个位置nums[1]，即需要把nums[i]放在nums[nums[i] - 1]上，那么我们遍历整个数组，如果nums[i] != i + 1, 而nums[i]为整数且不大于n，
另外nums[i]不等于nums[nums[i] - 1]的话，我们将两者位置调换，如果不满足上述条件直接跳过，最后我们再遍历一遍数组，如果对应位置上的数不正确则返回正确的数.
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, A):
        length = len(A)
        for i in xrange(length):
            while A[i] != i + 1:
                if A[i] <= 0 or A[i] > length or A[i] == A[A[i]-1]: break
                # swap A[i], A[A[i]-1]
                t = A[A[i]-1]; A[A[i]-1] = A[i]; A[i] = t
        for i in xrange(length):
            if A[i] != i + 1:
                return i + 1
        return length + 1


    	# http://heai.info/2014-10/markdown-leetcode-first-missing-positive/
    	# A[i] = i + 1 ==> A[i] - 1 = i
    	# ==> A[i] = A[A[i]-1] 
    	# ==> A[A[i]-1] = A[i]

# ***** The Second Time ********
# 题目给出1到N的正整数，但是不全，里面也可能混着0和负整数，找出第一个缺失的正整数。
# 要求时间O(N)空间固定，可使用原数组，通过交换元素使得A[i] = i + 1，第二次遍历时不满足
# A[i] = i + 1的就是要找的数。
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while nums[i] ! = i + 1:
                if nums[i]<=0 or nums[i] > n or nums[i] == nums[nums[i]-1]:
                    break
                tmp = nums[i]; nums[i] = nums[nums[i]-1] ; nums[nums[i]-1] = tmp
                # 交换元素的推导在上面

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1  #最后一个元素的下一个
        

























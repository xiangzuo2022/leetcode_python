"""
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res_dict = {i:-1 for i in nums2}
        for i in nums2:
            while stack and i > stack[-1]:
                small = stack.pop()
                res_dict[small] = i
            stack.append(i)
        res = []
        for j in nums1:
            res.append(res_dict[j])
        return res
      
      
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        d, stack = {}, []
        for num2 in nums2:
            while stack and num2 > stack[-1]:
                d[stack.pop()] = num2
            stack.append(num2)
        return [d.get(j, -1) for j in nums1]

作者：qingfengpython
链接：https://leetcode-cn.com/problems/next-greater-element-i/solution/496xia-yi-ge-geng-da-yuan-su-i-by-qingfe-qfu9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# https://www.youtube.com/watch?v=68a1Dc_qVq4
"""
O(n*m) time complexity and O(m) memory complexity by using hashmap
"""
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        n = len(nums2)

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res
    
# using monotic stack O(m+n) time complexity
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        n = len(nums2)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res
    
"""
using nums1 to build up a hashmap for the elements map to its indexes
"""


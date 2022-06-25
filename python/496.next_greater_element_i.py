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
"""
不是最优解， 因为用了额外的空间
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
    	d = {}
    	for i in range(len(nums)):
    		if nums[i] not in d:
    			d[nums[i]] = 1
    		else:
    			d[nums[i]] += 1
    	for key in d:
    		if d[key] == 1:
    			return key



"""
# ******** 优化的解法 **********
#很简单，就是位操作，任意两个相同的数如果做异或(Exclusive Or)运算的话，结果为0.所以，
# 这题的解法就是这么直白，从0开始到n，一路异或下去，最后剩下的值就是所求。
答案是使用位运算。对于这道题，可使用异或运算 ⊕\oplus⊕。异或运算有以下三个性质。

任何数和 000 做异或运算，结果仍然是原来的数，即 a⊕0=aa \oplus 0=aa⊕0=a。
任何数和其自身做异或运算，结果是 000，即 a⊕a=0a \oplus a=0a⊕a=0。
异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=ba \oplus b \oplus a=b \oplus a \oplus a=b \oplus (a \oplus a)=b \oplus0=ba⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
""" 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
     
        ans = 0
        for i in range(0,len(nums)):
            ans = ans ^ nums[i] 
        return ans
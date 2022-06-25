"""
# *********** The Second Time ********
# 解题思路：这道题不允许使用排序库函数。那么最直观的解法是：遍历两遍数组，第一遍对0，1，2计数，
# 第二遍对数组进行赋值，这样是可以ac的。但题目的要求是只使用常数空间，而且只能遍历一遍。那么思路就比较
# 巧妙了。设置两个头尾指针，头指针p0指向的位置是0该放置的位置，尾指针p2指向的位置是2该放置的位置。
# i用来遍历整个数组，碰到0把它和p0指向的数交换，碰到2把它和p2指向的数交换，碰到1继续向后遍历。
# 有点类似快速排序的分割数组这一步。
"""

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
    	if not nums:
    		return 
    	p0 = 0; p2 = len(nums)-1; i = 0
    	while i <= p2:
    		if nums[i] == 0:
    			nums[i],nums[p0] = nums[p0], nums[i]
    			i += 1
    			p0 += 1
    		elif nums[i] == 2:
    			nums[i],nums[p2] = nums[p2],nums[i]
    			p2 -= 1
    		else:
    			i += 1



#  The fourth Time

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums); red = 0; blue = n -1; i = 0
        while i <= blue: #开始错才这里写成 n-1
            if nums[i] == 0:
                nums[i],nums[red] = nums[red],nums[i]
                i += 1
                red += 1
            elif nums[i] == 2:
                nums[i],nums[blue] = nums[blue],nums[i]
                blue -= 1 # ==2时i不变 
                
            else:
                i+=1

"""
another implementation by using two pointers
我们也可以考虑使用指针 p0  来交换 0，p2来交换 2。此时，p0
​
  的初始值仍然为 00，而 p_2p 
2
​
  的初始值为 n-1n−1。在遍历的过程中，我们需要找出所有的 00 交换至数组的头部，并且找出所有的 22 交换至数组的尾部。

由于此时其中一个指针 p_2p 
2
​
  是从右向左移动的，因此当我们在从左向右遍历整个数组时，如果遍历到的位置超过了 p_2p 
2
​
 ，那么就可以直接停止遍历了。

具体地，我们从左向右遍历整个数组，设当前遍历到的位置为 ii，对应的元素为 \textit{nums}[i]nums[i]；

如果找到了 00，那么与前面两种方法类似，将其与 \textit{nums}[p_0]nums[p 
0
​
 ] 进行交换，并将 p_0p 
0
​
  向后移动一个位置；

如果找到了 22，那么将其与 \textit{nums}[p_2]nums[p 
2
​
 ] 进行交换，并将 p_2p 
2
​
  向前移动一个位置。

这样做是正确的吗？可以发现，对于第二种情况，当我们将 \textit{nums}[i]nums[i] 与 \textit{nums}[p_2]nums[p 
2
​
 ] 进行交换之后，新的 \textit{nums}[i]nums[i] 可能仍然是 22，也可能是 00。然而此时我们已经结束了交换，开始遍历下一个元素 \textit{nums}[i+1]nums[i+1]，不会再考虑 \textit{nums}[i]nums[i] 了，这样我们就会得到错误的答案。

因此，当我们找到 22 时，我们需要不断地将其与 \textit{nums}[p_2]nums[p 
2
​
 ] 进行交换，直到新的 \textit{nums}[i]nums[i] 不为 22。此时，如果 \textit{nums}[i]nums[i] 为 00，那么对应着第一种情况；如果 \textit{nums}[i]nums[i] 为 11，那么就不需要进行任何后续的操作。

"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/sort-colors/solution/yan-se-fen-lei-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。







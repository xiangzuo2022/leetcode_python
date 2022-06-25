"""
# 解题思路：模拟法。开辟一个数组leftmosthigh，leftmosthigh[i]为A[i]之前的最高的bar值，然后从后面开
# 始遍历，用rightmax来记录从后向前遍历遇到的最大bar值，那么min(leftmosthigh[i], 
# rightmax)-A[i]就是在第i个bar可以储存的水量。例如当i=9时，此时leftmosthigh[9]=3,而rightmax=2，
# 则储水量为2-1=1，依次类推即可。这种方法还是很巧妙的。时间复杂度为O(N)。
# height[i]的储水量与前后bar有关， 所以要leftmosthight and rightmax.
"""

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
    	leftmosthigh = [0 for i in range(len(height))]
    	leftmax = 0
    	for i in range(len(height)):
    		if height[i] > leftmax:
    			leftmax = height[i]
    		leftmosthigh[i] = leftmax
    	sum = 0
    	rightmax = 0
    	for i in reversed(range(len(height))):
    		if height[i] > rightmax:
    			rightmax = height[i]
    		if min(rightmax,leftmosthigh[i]) > height[i]:
    			sum += min(rightmax,leftmosthighp[i]) - height[i]
    	return sum



"""
九章solution的实现：two pointers是solution， 实现时从指针值小的那边灌水
强化班视频讲解很好 3-2
"""
class Solution(object):
    def trap(self, bars):
        if not bars or len(bars) < 2:
            return 0
        volume = 0
        left, right = 0, len(bars) - 1
        l_max, r_max = bars[left], bars[right]
        while left < right:
            l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
            if l_max <= r_max:
                volume += l_max - bars[left]
                left += 1
            else:
                volume += r_max - bars[right]
                right -= 1
        return volume


"""
单调栈法
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # "两头大小决定中间"的题目，考虑使用单调栈来解决，
        # 类似于84题"柱状图中最大矩形"，但注意两题中所求面积不同导致的代码差异，84题求各最大值，而本题求和
        stack = []            # 欲维护一个递减栈，注意我们的栈中保存元素下标
        res = 0

        for i in range(len(height)):

            # 新比较的元素比栈顶元素大 ---> 栈顶元素的右边界已找到，
            # 又因为我们维护了一个递减栈，栈顶下面的元素高度也大于他，即栈顶处形成凹陷，可计算面积
            while stack and height[i] > height[stack[-1]]:

                # 记录栈顶的元素并出栈，接下来我们已经得知栈顶的左右边界，可计算此元素的面积
                top = stack.pop()
                if not stack: break          # 把栈顶弹出后栈空，即其左边没有比他大的了，无法接水

                # 栈顶值面积，宽: 右(即为新比较的元素) - 左(弹出后stack-1即为其左) - 1
                # 长：左右高柱中较矮的柱子  - 栈顶高度
                # 每次面积实际上仅仅是"本元素可接的水的面积"，又因为出栈，不会重复计算， += 计算总面积。相关面积可参考甜姨动图理解
                res += (i - stack[-1] - 1) * (min(height[i], height[stack[-1]]) - height[top])

            stack.append(i)           # 新比较的元素比栈顶元素矮 ---> 未找到右边界，没形成凹陷。 将新比较的元素入该单减栈
        return res

作者：miss-right
链接：https://leetcode-cn.com/problems/trapping-rain-water/solution/dan-jian-zhan-pythondai-ma-zui-quan-zhu-c90ln/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
DP
"""
















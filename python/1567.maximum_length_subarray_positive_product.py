"""
DP solution:可以使用动态规划得到乘积为正数的最长子数组长度。定义两个数组 \textit{positive}positive 和 \textit{negative}negative，其中 \textit{positive}[i]positive[i] 表示以下标 ii 结尾的乘积为正数的最长子数组长度，\textit{negative}[i]negative[i] 表示乘积为负数的最长子数组长度。
链接：https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product/solution/cheng-ji-wei-zheng-shu-de-zui-chang-zi-shu-zu-ch-3/
"""
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        length = len(nums)
        positive, negative = [0] * length, [0] * length
        if nums[0] > 0:
            positive[0] = 1
        elif nums[0] < 0:
            negative[0] = 1
        
        maxLength = positive[0]
        for i in range(1, length):
            if nums[i] > 0:
                positive[i] = positive[i - 1] + 1
                negative[i] = (negative[i - 1] + 1 if negative[i - 1] > 0 else 0)
            elif nums[i] < 0:
                positive[i] = (negative[i - 1] + 1 if negative[i - 1] > 0 else 0)
                negative[i] = positive[i - 1] + 1
            else:
                positive[i] = negative[i] = 0
            maxLength = max(maxLength, positive[i])

        return maxLength

"""
注意到 \textit{positive}[i]positive[i] 和 \textit{negative}[i]negative[i] 的值只与 \textit{positive}[i-1]positive[i−1] 和 \textit{negative}[i-1]negative[i−1] 有关，因此可以使用滚动数组优化空间。

"""
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        length = len(nums)
        positive, negative = int(nums[0] > 0), int(nums[0] < 0)
        maxLength = positive

        for i in range(1, length):
            if nums[i] > 0:
                positive += 1
                negative = (negative + 1 if negative > 0 else 0)
            elif nums[i] < 0:
                newPositive = (negative + 1 if negative > 0 else 0)
                newNegative = positive + 1
                positive, negative = newPositive, newNegative
            else:
                positive = negative = 0
            maxLength = max(maxLength, positive)

        return maxLength



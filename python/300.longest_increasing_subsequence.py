"""
dp[i]表示前i个数以i结尾的最长上升序列是多少
不要求是连续的 O(n^2)
思路与算法

定义 dp[i]\textit{dp}[i]dp[i] 为考虑前 iii 个元素，以第 iii 个数字结尾的最长上升子序列的长度，注意 nums[i]\textit{nums}[i]nums[i] 必须被选取。

我们从小到大计算 dp\textit{dp}dp 数组的值，在计算 dp[i]\textit{dp}[i]dp[i] 之前，我们已经计算出 dp[0…i−1]\textit{dp}[0 \ldots i-1]dp[0…i−1] 的值，则状态转移方程为：

dp[i]=max(dp[j])+1,其中0≤j<i且num[j]<num[i]\textit{dp}[i] = \max(\textit{dp}[j]) + 1, \text{其中} \, 0 \leq j < i \, \text{且} \, \textit{num}[j]<\textit{num}[i]
dp[i]=max(dp[j])+1,其中0≤j<i且num[j]<num[i]

即考虑往 dp[0…i−1]\textit{dp}[0 \ldots i-1]dp[0…i−1] 中最长的上升子序列后面再加一个 nums[i]\textit{nums}[i]nums[i]。由于 dp[j]\textit{dp}[j]dp[j] 代表 nums[0…j]\textit{nums}[0 \ldots j]nums[0…j] 中以 nums[j]\textit{nums}[j]nums[j] 结尾的最长上升子序列，所以如果能从 dp[j]\textit{dp}[j]dp[j] 这个状态转移过来，那么 nums[i]\textit{nums}[i]nums[i] 必然要大于 nums[j]\textit{nums}[j]nums[j]，才能将 nums[i]\textit{nums}[i]nums[i] 放在 nums[j]\textit{nums}[j]nums[j] 后面以形成更长的上升子序列。

最后，整个数组的最长上升子序列即所有 dp[i]\textit{dp}[i]dp[i] 中的最大值。

LISlength=max(dp[i]),其中0≤i<n\text{LIS}_{\textit{length}}= \max(\textit{dp}[i]), \text{其中} \, 0\leq i < n
LIS 
length
​
 =max(dp[i]),其中0≤i<n

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in range (1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


"""
O(nlogn) 维护一个单调序列, 遍历nums数组，二分查找每一个数在单调序列中的位置，然后替换之。
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append(nums[x])
            else:
                dp[low] = nums[x]
        return len(dp)


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        size = len(nums)
        ans = []

        for x in range(size):
            low = 0
            high = len(ans)-1

            while low <= high:

                mid = (low+high)/2

                if ans[mid] < nums[x]:  
                    low = mid+1
                else:
                   
                    high = mid-1

            if low >= len(ans):  
                ans.append(nums[x])
            else: 
                ans[low] = nums[x]
        return len(ans)







        

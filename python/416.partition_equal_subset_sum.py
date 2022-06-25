01背包问题
背包问题，大家都知道，有N件物品和一个最多能被重量为W 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。
每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
背包问题有多种背包方式，常见的有：01背包、完全背包、多重背包、分组背包和混合背包等等。
要注意题目描述中商品是不是可以重复放入。
即一个商品如果可以重复多次放入是完全背包，而只能放入一次是01背包，写法还是不一样的。
要明确本题中我们要使用的是01背包，因为元素我们只能用一次。

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumAll = sum(nums)
        if sumAll % 2:
            return False
        target = sumAll // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[-1]

作者：edelweisskoko
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/416-fen-ge-deng-he-zi-ji-dong-tai-gui-hu-csk5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        taraget = sum(nums)
        if taraget % 2 == 1: return False
        taraget //= 2
        dp = [0] * 10001
        for i in range(len(nums)):
            for j in range(taraget, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        return taraget == dp[taraget]
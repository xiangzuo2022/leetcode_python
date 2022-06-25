本题也是DP算法，定义f[i]表示以到i元素为止的等差数列个数。因为等差数列只有3个和3个元素以上才有等差的意义因此，我们从f[2]开始往后计算。

当A[i] - A[i-1] = A[i-1] - A[i-2]时，表示至少过去3个元素是等差数列。这是新增的，且f[i-1]如果不为0，则表示在过去3个元素中，有延续。

f[i] = f[i-1] + 1若过去三个元素是等差。

作者：idealworld
链接：https://leetcode-cn.com/problems/arithmetic-slices/solution/pythondong-tai-gui-hua-suan-fa-by-idealworld/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # 至少3个才叫数列，才有等差这种概念
        # f[i]表示到i元素为止的等差数列个数，差（d）是一样的
        # A[i] - A[i-1]等于A[i-1] - A[i-2]，则f[i] = f[i-1] + 1
        # 从左往右更新
        n = len(A)
        f = [0] * n
        
        if n < 3:
            return 0
        
        # f[0], f[1], f[2]
        for i in range(2, n):
            if A[i] - A[i-1] ==  A[i-1] - A[i-2]:
                f[i] = f[i-1] + 1
        # print(f)
        return sum(f)

作者：idealworld
链接：https://leetcode-cn.com/problems/arithmetic-slices/solution/pythondong-tai-gui-hua-suan-fa-by-idealworld/

题目大概意思是 每次move会移除一块行或列存在其他石头的石头(一次只移除一块石头，这块石头满足行或列有其他石头) 问最多可以移除多少块

并查集 disjoint set is used for checking whether a circle is exist in a graph.
Find(x): find the root of cluster x
Union(x): merge two clusters

方法二： 并查集
思路

在方法一中，我们通过深度优先搜索来计算隐式图中连通分量的个数。实际上有更高效的解决方法，那就是用并查集。

算法

对于一个坐标为 (i, j) 的石子来说，需要把行 i 和列 j 合并，因为并查集是一维的，用 j+10000 来代替 j。在将所有石子的行和列都合并好之后，只需数一下并查集中有几个集合就可以得到答案了。

简洁起见，这里实现的并查集就不根据 rank 来合并了。因此渐进复杂度会比用 rank 的高一点。

作者：LeetCode
链接：https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/solution/yi-chu-zui-duo-de-tong-xing-huo-tong-lie-shi-tou-b/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class DSU:
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr

class Solution(object):
    def removeStones(self, stones):
        N = len(stones)
        dsu = DSU(20000)
        for x, y in stones:
            dsu.union(x, y + 10000)

        return N - len({dsu.find(x) for x, y in stones})


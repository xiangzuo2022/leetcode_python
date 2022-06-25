"""
方法一：排序
思路和算法
将每个点到原点的欧几里得距离的平方从小到大排序后，取出前 kk 个即可。
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:k]

"""
quick sort
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def random_select(left: int, right: int, k: int):
            pivot_id = random.randint(left, right)
            pivot = points[pivot_id][0] ** 2 + points[pivot_id][1] ** 2
            points[right], points[pivot_id] = points[pivot_id], points[right]
            i = left - 1
            for j in range(left, right):
                if points[j][0] ** 2 + points[j][1] ** 2 <= pivot:
                    i += 1
                    points[i], points[j] = points[j], points[i]
            i += 1
            points[i], points[right] = points[right], points[i]
            # [left, i-1] 都小于等于 pivot, [i+1, right] 都大于 pivot
            if k < i - left + 1:
                random_select(left, i - 1, k)
            elif k > i - left + 1:
                random_select(i + 1, right, k - (i - left + 1))

        n = len(points)
        random_select(0, n - 1, k)
        return points[:k]

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/k-closest-points-to-origin/solution/zui-jie-jin-yuan-dian-de-k-ge-dian-by-leetcode-sol/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
another quick sort implementation
"""
class Solution(object):
    def kClosest(self, points, K):
        results = []
        for i in range(len(points)):
            points[i] = (points[i][0]**2 + points[i][1]**2, points[i])  # (distance, point) tuple
        self.quickSelectHelper(points, 0, len(points)-1, K)
        for i in range(K):
            results.append(points[i][1])
        return results

    def quickSelectHelper(self, arr, start, end, K):
        if start >= end: return
        i, j = start + 1, end
        while i <= j:
            while i <= j and arr[i][0] <= arr[start][0]:  # compare the first element in tuple (distance)
                i += 1
            while i <= j and arr[j][0] >= arr[start][0]:  # compare the first element in tuple (distance)
                j -= 1
            if i < j: arr[i], arr[j] = arr[j], arr[i]
        arr[start], arr[j] = arr[j], arr[start]
        if K == j:
            return
        elif K < j:
            self.quickSelectHelper(arr, start, j-1, K)
        else:
            self.quickSelectHelper(arr, j+1, end, K)
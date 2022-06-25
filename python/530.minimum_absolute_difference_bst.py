"""
递归中序遍历成为递增数组，然后在数组中做
"""
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = []   
        r = float("inf")
        def buildaList(root):  //把二叉搜索树转换成有序数组
            if not root: return None
            if root.left: buildaList(root.left)  //左
            res.append(root.val)  //中
            if root.right: buildaList(root.right)  //右
            return res
            
        buildaList(root)
        for i in range(len(res)-1):  // 统计有序数组的最小差值
            r = min(abs(res[i]-res[i+1]),r)
        return r
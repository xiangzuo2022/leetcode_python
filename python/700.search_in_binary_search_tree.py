class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val: return root  //为空或者已经找到都是直接返回root，所以合并了
        if root.val > val: return self.searchBST(root.left,val)  //注意一定要加return
        else: return self.searchBST(root.right,val)  
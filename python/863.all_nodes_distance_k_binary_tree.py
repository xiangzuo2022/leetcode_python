"""
首先需要为每个节点记录他们的父亲节点，这一点很容易想到哈希表，在递归找左右孩子的时候加上找父亲那一条路的方法即可。
需要注意的是，如果只是向下寻找，而不返回父亲的话，是不可能出现重复的（因为只向下走），但是有了向父亲的走向，就会存在重复。

"""
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        maps={}#构建哈希表，记录每个节点的父亲节点
        def findP(root):
            if root.left:
                maps[root.left.val]=root
                findP(root.left)
            if root.right:
                maps[root.right.val]=root
                findP(root.right)
        res=[]
        def dfs(root,node,k):
            '''
            需要记录上一个遍历的节点是啥，防止5-->3 然后 3又去左子树5  这样走了两步
            '''
            if k==0:
                res.append(root.val)
                return 
            if root.left and root.left!=node:#左
                dfs(root.left,root,k-1)
            if root.right and root.right!=node:#右
                dfs(root.right,root,k-1)
            if root.val in maps and maps[root.val]!=node:#父亲 (search up)
                dfs(maps[root.val],root,k-1)
        findP(root)
        dfs(target,None,k)
        return res

作者：enghishyang
链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/solution/er-cha-shu-zhong-suo-you-ju-chi-wei-kde-nlct0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        maps = {}
        ans = []
        def findParent(root):
            if root.left:
                maps[root.left.val] = root
                findParent(root.left)
            if root.right:
                maps[root.right.val] = root
                findParent(root.right)
        def dfs(root, node, k):
            if k == 0:
                ans.append(root.val)
                return 
            if root.left and root.left != node:
                dfs(root.left, root, k-1)
            if root.right and root.right != node:
                dfs(root.right, root, k-1)
            if root.val in maps and maps[root.val] != node:
                dfs(maps[root.val], root, k-1)
        findParent(root)
        dfs(target, None, K)
        return ans
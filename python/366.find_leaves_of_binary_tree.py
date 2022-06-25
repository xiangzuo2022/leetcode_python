"""
这道题给了我们一个二叉树，让我们返回其每层的叶节点，就像剥洋葱一样，将这个二叉树一层一层剥掉，最后一个剥掉根节点。那么题目中提示说要用DFS来做，思路是这样的，
每一个节点从左子节点和右子节点分开走可以得到两个深度，由于成为叶节点的条件是左右子节点都为空，所以我们取左右子节点中较大值加1为当前节点的深度值，
知道了深度值就可以将节点值加入到结果res中的正确位置了
"""
def findLeaves(self, root):
    ret = []
    def dfs(node):
        if not node:
            return 0
        depth = max(dfs(node.left),dfs(node.right))+1
        if len(ret)<depth:
            ret.append([])
        ret[depth-1].append(node.val)
        return depth
    dfs(root)
    return ret
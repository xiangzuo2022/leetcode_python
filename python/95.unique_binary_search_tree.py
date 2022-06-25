题解
卡特兰数问题

递归
二叉排序树的重要性质是，左子树上的节点值一定小于根节点，右子树上的节点值一定大于根节点。由此，可知若根节点为ii，则左子树的节点为[1,...,i-1][1,...,i−1]，右子树的节点为[i+1,...,n][i+1,...,n]。可递归的构建二叉搜索树。
特判，若n==0，返回[][]
定义生成树函数build_Trees(left,right)build_Trees(left,right)，表示生成[left,...,right][left,...,right]的所有可能二叉搜索树：

若left>right，说明为空树，返回[None]
初始化所有可能的二叉搜索树列表all_trees=[]
遍历每一种可能的节点ii，遍历区间[left,right+1):
所有可能的左子树列表left_trees=build_Trees(left,i-1)
所有可能的右子树列表right_trees=build_Trees(i+1,right)
组合所有的方式，遍历左子树列表,l：遍历右子树列表,r
建立当前树节点cur_tree=TreeNode(i)cur_tree=TreeNode(i)
将cur_treecur_tree左子树置为l
将cur_treecur_tree右子树置为r
将cur_treecur_tree加入树列表中
返回树列表all_treesall_trees
返回build_Trees(1,n)
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/di-gui-zhu-xing-jie-shi-python3-by-zhu_shi_fu/

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if(n==0):
            return []
        def build_Trees(left,right):
            all_trees=[]
            if(left>right):
                return [None]
            for i in range(left,right+1):
                left_trees=build_Trees(left,i-1)
                right_trees=build_Trees(i+1,right)
                for l in left_trees:
                    for r in right_trees:
                        cur_tree=TreeNode(i)
                        cur_tree.left=l
                        cur_tree.right=r
                        all_trees.append(cur_tree)
            return all_trees
        res=build_Trees(1,n)
        return res


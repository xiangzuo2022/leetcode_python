# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def iterative_inorder(self,root,list):
    	stack = []
    	while root or stack:
    		if root:
    			stack.append(root)
    			root = root.left
    		else:
    			root = stack.pop()
    			list.append(root.val)
    			root = root.right
    	return list


    def inorderTraversal(self, root):
    	list = []
    	self.iterative_inorder(root,list)
    	return list
    	
# 题意：二叉树的中序遍历。这道题用递归比较简单，考察的是非递归实现二叉树中序遍历。
# 中序遍历顺序为：左子树，根，右子树。如此递归下去。


"""
# *********** The Second Time **********
# 题意：二叉树的中序遍历。这道题用递归比较简单，考察的是非递归实现二叉树中序遍历。中序遍历顺序为：
# 左子树，根，右子树。如此递归下去。
# 解题思路：假设树为：

　　　　　　　　　　　　　　　　1

　　　　　　　　　　　　　　　/　  \

　　　　　　　　　　　　　　 2　　  3

　　　　　　　　　　　　　  /   \　 /   \

   　　　　　　　　　　　　4     5  6    7

# 我们使用一个栈来解决问题。步骤如下：
# 一，我们将根节点1入栈，如果有左孩子，依次入栈，那么入栈顺序为：1，2，4。由于4的左子树为空，停止入栈，
# 此时栈为{1，2，4}。
# 二，此时将4出栈，并遍历4，由于4也没有右孩子，那么根据中序遍历的规则，我们显然应该继续遍历4的父亲2，
# 情况是这样。所以我们继续将2出栈并遍历2，2存在右孩子，将5入栈，此时栈为{1，5}。
# 三，5没有孩子，则将5出栈并遍历5，这也符合中序遍历的规则。此时栈为{1}。
# 四，1有右孩子，则将1出栈并遍历1，然后将右孩子3入栈，并继续以上三个步骤即可。
# 栈的变化过程：{1}->{1,2}->{1,2,4}->{1,2}->{1}->{1,5}->{1}->{}->{3}->{3,6}->{3}->{}->{7}->{}。
""""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def iterative_inorder(self,root,ans):
        stack = []
        while root or stack:#中序遍历开始stack里没root是空的， 所以判断条件要加上root 
            if root:
                stack.append(root)  # 先要visit left 所以root先压入栈
                root = root.left
            else:# 一旦左边为空， 弹出的元素优先为左结点，然后是root， 最后是right
                root = stack.pop()
                ans.append(root.val)
                root = root.right
        return ans

    def inorderTraversal(self, root):
        ans = []
        self.iterative_inorder(root,list)
        return list

#  解法二： 递归
    def recursive_inorder(self,root,list):
        if root:
            self.recursive_inorder(root.left, list)
            list.append(root.val)
            self.recursive_inorder(root.right,list)

    def inorderTraversal(self, root):
        list = []
        self.recursive_inorder(root,list)
        return list

"""
more concise code
"""
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder = []
        if not root: return inorder
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                inorder.append(root.val)
                root = root.right
        return inorder




















"""
网上的解法
"""

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(kid)] or [str(root.val)]


"""
My own solution 
"""
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        Solution.ans = []
        self.paths(root,'')
        return Solution.ans
        
    def paths(self,root,tmp):
        if not root:return []
        tmp += str(root.val) + '->'
        if not root.left and not root.right:            
            Solution.ans.append(tmp[:-2])
        return self.paths(root.left,tmp) + self.paths(root.right,tmp)
      
"""
DFS递归
"""
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    ans.append(path)
                else:
                    path += '->'
                    dfs(root.left, path)
                    dfs(root.right, path)
        ans = []
        dfs(root, '')
        return ans
      
      
"""
BFS
"""
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = list()
        if not root:
            return paths

        node_queue = collections.deque([root])
        path_queue = collections.deque([str(root.val)])

        while node_queue:
            node = node_queue.popleft()
            path = path_queue.popleft()

            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + '->' + str(node.left.val))
                
                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + '->' + str(node.right.val))
        return paths

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/binary-tree-paths/solution/er-cha-shu-de-suo-you-lu-jing-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
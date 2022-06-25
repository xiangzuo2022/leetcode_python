"""
这道题让我们竖直遍历二叉树，并把每一列存入一个二维数组，我们看题目中给的第一个例子，3和15属于同一列，3在前，
第二个例子中，3,5,2在同一列，3在前，5和2紧随其后，那么我们隐约的可以感觉到好像是一种层序遍历的前后顺序，
那么我们如何来确定列的顺序呢，我们可以把根节点给个序号0，然后开始层序遍历，凡是左子节点则序号减1，
右子节点序号加1，这样我们可以通过序号来把相同列的节点值放到一起，我们用一个TreeMap来建立序号和其对应的节点
值的映射，用TreeMap的另一个好处是其自动排序功能可以让我们的列从左到右，由于层序遍历需要用到queue，
我们此时queue里不能只存节点，而是要存序号和节点组成的pair，这样我们每次取出就可以操作序号，
而且排入队中的节点也赋上其正确的序号.
"""
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]
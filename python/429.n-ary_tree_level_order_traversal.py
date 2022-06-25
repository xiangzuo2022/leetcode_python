"""
# 这个地方要用extend而不是append，我们看下面的例子：
                    # In [18]: alist=[]
                    # In [19]: alist.append([1,2,3])
                    # In [20]: alist
                    # Out[20]: [[1, 2, 3]]
                    # In [21]: alist.extend([4,5,6])
                    # In [22]: alist
                    # Out[22]: [[1, 2, 3], 4, 5, 6]
                    # 可以看到extend对要添加的list进行了一个解包操作
                    # print(root.children)，可以得到children是一个包含
                    # 孩子节点地址的list，我们使用for遍历quene的时候，
                    # 希望quene是一个单层list，所以要用extend
                    # 使用extend的情况，如果print(quene),结果是
                    # deque([<__main__.Node object at 0x7f60763ae0a0>])
				   # deque([<__main__.Node object at 0x7f607636e6d0>, <__main__.Node object at 0x7f607636e130>, <__main__.Node object at 0x7f607636e310>])
				  # deque([<__main__.Node object at 0x7f607636e880>, <__main__.Node object at 0x7f607636ef10>])
				  # 可以看到是单层list
                    # 如果使用append，print(quene)的结果是
                    # deque([<__main__.Node object at 0x7f18907530a0>])
				  # deque([[<__main__.Node object at 0x7f18907136d0>, <__main__.Node object at 0x7f1890713130>, <__main__.Node object at 0x7f1890713310>]])
				  # 可以看到是两层list，这样for的遍历就会报错

"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        queue = [root]
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)                
                queue.extend(node.children)
            result.append(level)
        return result
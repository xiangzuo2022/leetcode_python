"""
O(1) space 
"""
class Solution:
    def __init__(self):
        # 记录上一个节点值，初始值为null是为了判断当前节点是否是第一个节点
        self.pre = None
        # 存储众数的数组
        self.ret = []
        # 众数的个数，也就是数组长度
        self.ret_count = 0
        # 二叉树中节点最大出现次数
        self.max_count = 0
        # 当前节点的值的最大出现次数
        self.cur_count = 0

    def findMode(self, root: TreeNode) -> List[int]:
        self.inOrder(root)
        self.pre = None
        self.ret = [0] * self.ret_count
        self.ret_count, self.cur_count = 0, 0
        self.inOrder(root)
        return self.ret

    def inOrder(self, root: TreeNode) -> None:
        if not root:
            return
        self.inOrder(root.left)
        # 中序遍历，搜索二叉树增序
        # 当前节点值等于前一个节点的值，这个值的出现次数+1
        if self.pre and self.pre.val == root.val:
            self.cur_count += 1
        else:
            # 如果当前节点是第一个节点或者当前节点值不等于前一个节点，那么这个值的出现次数记为1
            self.cur_count = 1
        # 如果当前值的出现次数比最大出现次数还要大，那么说明当前值才是出现最多的众数，因此数组个数记为1
        if self.cur_count > self.max_count:
            self.max_count = self.cur_count
            self.ret_count = 1
        elif self.cur_count == self.max_count:
            # 这一步是为了第二次调用时给数组赋值用的
            # 第一次调用计算得出了最大出现次数，那么第二次调用时，发现当前值的最大出现次数==第一次得出的最大出现次数，那么这个值肯定是众数之一
            
            if len(self.ret):
                self.ret[self.ret_count] = root.val
            # 如果当前值的出现次数等于最大出现次数，那么说明有多个众数，数组个数+1
            self.ret_count += 1
        # 更新pre值
        self.pre = root
        self.inOrder(root.right)

作者：faterazer
链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/solution/zhen-zheng-fu-he-ti-mu-yao-qiu-de-o1kong-jian-fu-z/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
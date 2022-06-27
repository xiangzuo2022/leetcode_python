"""
# 题目给出了一个特殊的单链表。链表的每一个节点多了个指针域: random. 随机指向链表的某一个node。
# 题目要求我们给出这个链表的一个 deep copy.
首先，何为 deep copy ??
Part 1:  三种 Object Copy 的对比(以 Array 为例)
1. Shallow copy
拷贝时仅仅复制的是 指针 或者 引用， 也就是说 数据仅存在一份。
当然，得到效率的同时，存在的问题就是，如果原来的数据改变了， 复制后的对象也改变了，因为仅仅存在一份数据!!!
Note: 其实是出于效率的考虑，在某些场合，并不需要多份数据时，可以采用 shallow copy
2. Deep copy
与 shallow copy 不同，deep copy 复制后，数据有多份。因此， deep copy 也比较费时。
在 C++ 中，可以自行定义类的 copy 构造函数来实现 deep copy.
Python 中，array 默认的复制是 shallow copy,  可以采用 copy 模块的 deep copy

http://blog.csdn.net/shoulinjun/article/details/18730871

"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None: return None
        tmp = head
        while tmp: # 这个loop插入相同的节点到原节点后面
            newNode = RandomListNode(tmp.label)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next # 因为复制了一个原节点， 要往后移动2个
        tmp = head
        while tmp: # this loop gives random pointer 
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next
        # 开始分离一个链表成两个
        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None


"""
九章solution, 思路非常清晰，比起hashmap没有耗费过多的空间
"""
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:return None
        self.copyNext(head)
        self.copyRandom(head)
        return splitList(head)


    def copyNext(self,head):
        while head:
            newNode = RandomListNode(head.label)
            newNode.random = head.random
            newNode.next = head.next
            head.next = newNode
            head = head.next.next

    def copyRandom(self,head):
        while head:
            if head.next.random:
                head.next.random = head.random.next
            head = head.next.next 

    def splitList(self,head):
        newHead = head.next
        while head:
            tmp = head.next
            head.next = tmp.next
            head = head.next
            if tmp.next:
                tmp.next = tmp.next.next
        return newHead



"""
九章hashmap 的解法
题解：
如果要copy一个带有random pointer的list，主要的问题就是有可能这个random指向的位置还没有被copy到，所以解决方法都是多次扫描list。
第一种方法，就是使用HashMap来坐，HashMap的key存原始pointer，value存新的pointer。
第一遍，先不copy random的值，只copy数值建立好新的链表。并把新旧pointer存在HashMap中。
第二遍，遍历旧表，复制random的值，因为第一遍已经把链表复制好了并且也存在HashMap里了，所以只需从HashMap中，把当前旧的node.random作为key值，
得到新的value的值，并把其赋给新node.random就好。
可以合并两遍scan为一个
"""
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:return None
        d = dict()
        dummy = ListNode(0);pre = dummy
        while head:
            if head in d:
                newNode = d[head]
            else:
                newNode = RandomListNode(head.label)
                d[head] = newNode
            pre.next = newNode

            if head.random:
                if head.random in d:
                    newNode.random = d[head.random]
                else:
                    newNode.random = RandomListNode(head.random.label)
                    d[head.random] = newNode.random
            pre = newNode
            head = head.next
        return dummy.next


"""
New version
"""
 Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:return None
        d = {}
        dummy = ListNode(0); pre = dummy
        while head:
            if head in d:
                newNode = d[head]
            else:
                newNode = Node(head.val,None, None)
                d[head] = newNode
            pre.next = newNode
            
            if head.random:
                if head.random in d:
                    newNode.random = d[head.random]
                else:
                    newNode.random = Node(head.random.val, None, None)
                    d[head.random] = newNode.random
            pre = newNode
            head = head.next
        return dummy.next


class Solution(object):
    def __init__(self):
        self.visitedHash = {}
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
   
        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

"""
Approach 1: https://leetcode.cn/problems/copy-list-with-random-pointer/solution/liang-chong-shi-xian-tu-jie-138-fu-zhi-dai-sui-ji-/
"""
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        p = head
        # 第一步，在每个原节点后面创建一个新节点
        # 1->1'->2->2'->3->3'
        while p:
            new_node = Node(p.val,None,None)
            new_node.next = p.next
            p.next = new_node
            p = new_node.next
        p = head
        # 第二步，设置新节点的随机节点
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        # 第三步，将两个链表分离
        p = head
        dummy = Node(-1,None,None)
        cur = dummy
        while p:
            cur.next = p.next
            cur = cur.next
            p.next = cur.next
            p = p.next
        return dummy.next

作者：wang_ni_ma
链接：https://leetcode.cn/problems/copy-list-with-random-pointer/solution/liang-chong-shi-xian-tu-jie-138-fu-zhi-dai-sui-ji-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。















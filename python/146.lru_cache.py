# define a doubly-linked list node
# http://www.cnblogs.com/zuoyuan/p/3701572.html
class Node:
	def __init__(self,key,val):
		self.key = key
		self.val = val
		self.prev = None
		self.next = None

class DoubleLinkedList:    #双向链表是一个表头，head指向第一个节点，tail指向最后一个节点
	def __init__(self):
		self.tail = None
		self.head = None

	def isEmpty():
		return not self.tail  #如果self.tail==None，那么说明双向链表为空

	def removeLast(self):  　　#删除tail指向的节点
		self.remove(self.tail)

	def remove(self,node):
		if self.head == self.tail:
			self.head, self.tail = None, None
			return
		if node == self.head:
			node.next.prev = None
			self.head = node.next
			return
		if node == self.tail:
			node.prev.next = None
			self.tail = node.prev
			return
		node.prev.next = node.next
		node.next.prev = node.prev

	def addFirst(self,node):   #在双向链表的第一个节点前面再插入一个节点　　
		if not self.head:
			self.head = self.tail = node
			node.prev = node.next = None
			return
		node.next = self.head
		self.head.prev = node
		self.head = node
		node.prev = None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
    	self.capacity = capacity
    	self.size = 0
    	self.d = dict()
    	self.cache = DoubleLinkedList()

        

    # @return an integer
    def get(self, key):
    	if key in self.d and self.cache[key]:
    		self.cache.remove(self.d[key])  #将key对应的指针指向的节点删除
    		self.cache.addFirst(self.d[key])  #然后将这个节点添加到双向链表头部
    		return self.d[key].val
    	else:
    		return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
    	if key in self.d:
    		self.cache.remove(self.d[key])
    		self.cache.addFirst(self.d[key])
    		self.d[key].val = value
    	else:
    		node = Node(key,value)
    		self.p[key] = value
    		self.cache.addFirst(node)
    		self.size += 1
    		if self.size > self.capacity:
    			self.size -= 1
    			del self.d[self.cache.tail.key]
    			self.cache.removeLast()

"""
# solution 2 使用Python的OrderedDict有序字典
# An OrderedDict is a dict that remembers the order that keys were first inserted. 
  If a new entry overwrites an existing entry, the original insertion position is left 
  unchanged. Deleting an entry and reinserting it will move it to the end.
  Python 2.7 中的OrderedDict 可以在迭代字典Items的时候保证按每项插入的顺序输出。
  当删除某项再用同样的key写入时，此项排在迭代的最后，同样是插入顺序排列的。
  可以用popitem的last=True/False来控制pop进返回最近插入的还是最早插入的，实际上就是维护了一个双向链表。
"""
class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
    	self.capacity = capacity
    	self.cache = collections.OrderedDict()
        

    # @return an integer
    def get(self, key):
    	if key not in self.cache:
    		return -1
    	value = self.cache.pop(key)
    	self.cache[key] = value # reinsert the key but the order index is changed
    	return value
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
    	if key in self.cache:
    		self.cache.pop(key)
    	elif len(self.cache) == self.capacity:
    		self.cache.popitem(last=False)
    	self.cache[key] = value

"""
jiuzhang solution: LinkedList 
"""
class LinkedNode:
    
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity
    
    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head
        
    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        if node.next is not None:
            self.hash[node.next.key] = prev
            node.next = None
        self.push_back(node)

    # @return an integer
    def get(self, key):
        if key not in self.hash:
            return -1
        self.kick(self.hash[key])
        return self.hash[key].next.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.hash:
            self.kick(self.hash[key])
            self.hash[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()
        

"""
official solution: 哈希表 + 双向链表
"""
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        # 使用伪头部和伪尾部节点    
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




















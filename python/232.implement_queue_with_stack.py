
"""
九章两个stack的解法
为了满足队列的 FIFO 的特性，我们需要用到两个栈，用它们其中一个来反转元素的入队顺序，用另一个来存储元素的最终顺序。
"""
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        
    def adjust(self):
        if len(self.stack2) == 0:
            while len(self.stack1)!=0:
                self.stack2.append(self.stack1.pop())
            
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.adjust()
        self.stack2.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self.adjust()
        return self.stack2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.stack1) and (not self.stack2)
        
"""
为了满足队列的 FIFO 的特性，我们需要用到两个栈，用它们其中一个来反转元素的入队顺序，用另一个来存储元素的最终顺序。
"""


# *********** The Second Time ********
# 两个stack要占用额外空间
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []
        

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)
        

    # @return nothing
    def pop(self):
        for x in range(len(self.queue)-1): # smart solution:除了最后一个元素外， 前面所有元素出占然后再进占，then the last element is in the front of the stack
            self.queue.append(self.queue.pop(0)) # queue只能从前面出
        self.queue.pop(0)  # 
        

    # @return an integer
    def top(self):
        return self.queue[-1]

    # @return an boolean
    def empty(self):
        return self.queue == []




















"""
思路：157的followup，需要用一个buf来存储上一次read4读入的字符，bufptr记录上一次读到的位置，
bufsize记录上一次read4读入buf的大小，通过这三个变量可以在多次读入的时候知道每次该从上一次的哪里继续读入字符，
以及何时再调用read4获取下一批字符。
"""
class Solution(object):
    def __init__(self):
        self.__buf4 = [''] * 4
        self.__i4 = 0
        self.__n4 = 0
 
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.__i4 < self.__n4:  # Any characters in buf4.
                buf[i] = self.__buf4[self.__i4]
                i += 1
                self.__i4 += 1
            else:
                self.__n4 = read4(self.__buf4)  # Read more characters.
                if self.__n4:
                    self.__i4 = 0
                else:  # Buffer has been empty.
                    break
 
        return i

"""
Read N Characters Given Read4 的拓展，之前只能调用一次，而这里可以调用多次，又多了一些corner case：
第一次调用时，如果read4读出的多余字符我们要先将其暂存起来，这样第二次调用时先读取这些暂存的字符;
第二次调用时，如果连暂存字符都没读完，那么这些暂存字符还得留给第三次调用时使用;
所以，难点就在于怎么处理这个暂存字符。因为用数组和指针控制对第二种情况比较麻烦，且这些字符满足先进先出，
所以我们可以用一个队列暂存这些字符。这样，只要队列不为空，就先读取队列。

defined share variables read_ and write_ to record positions read last time
"""

class Solution(object):
    def __init__(self):
        self.buffer = [''] * 4
        self.read_ = 0
        self.write_ = 0
 
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.read_ < self.write_:  # Any characters in buf4.
                buf[i] = self.buffer[self.read_]
                i += 1
                self.read_ += 1
            else:
                self.write_ = read4(self.buffer)  # Read more characters.
                if self.write_:
                    self.read_ = 0
                else:  # Buffer has been empty.
                    break
 
        return i
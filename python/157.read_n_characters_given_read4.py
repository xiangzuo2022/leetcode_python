"""
其实就是每次读4个，读出 n 个 拷贝到 char[] 里面去。
buf is used to store all characters that read 
"""


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        
        i = 0
        while i < n: 
            buf4 = ['','','','']
            count = read4(buf4) # Read file into buf4.
            if not count: break # EOF
            count = min(count, n - i) # be careful
            buf[i:] = buf4[:count] # Copy from buf4 to buf.
            i += count
        return i
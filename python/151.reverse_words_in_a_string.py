class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
    	return ' '.join([item for item in reversed(s.split(' ')) if item])


"""
My own solution:用了O(n)space不是最优解
"""
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):        
        a = s.split(" ")    
        b = []
        for i in a:
            if i != "":
                b.insert(0,i)      
        return ' '.join(b)

"""
最优解
"""
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):  
        return ' '.join(s.split()[::-1])

"""
所以解题思路如下：实现整个过程不用built-in Functions
移除多余空格
将整个字符串反转
将每个单词反转
"""
class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1
        
        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1
        
        # 将字符串间多余的空白字符去除
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        
        return output
            
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
            
    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0
        
        while start < n:
            # 循环至单词的末尾
            while end < n and l[end] != ' ':
                end += 1
            # 翻转单词
            self.reverse(l, start, end - 1)
            # 更新start，去找下一个单词
            start = end + 1
            end += 1
                
    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)
        
        # 翻转字符串
        self.reverse(l, 0, len(l) - 1)
        
        # 翻转每个单词
        self.reverse_each_word(l)
        
        return ''.join(l)


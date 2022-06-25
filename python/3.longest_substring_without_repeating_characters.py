"""
# 解法一：
# 解题思路：使用一个哈希表，记录字符的索引。例如对于字符串'zwxyabcabczbb'，
# 当检测到第二个'a'时，由于之前已经有一个'a'了，所以应该从第一个a的下一个字符重新开始测算长度，
# 但是要把第一个a之前的字符在哈希表中对应的值清掉，如果不清掉的话，就会误以为还存在重复的。
# 比如检测到第二个'z'时，如果第一个'z'对应的哈希值还在，那就出错了，所以要把第一个'a'之前的字符的哈
# 希值都重置才行。
"""


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
    	start = 0
        maxlen = 0
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = -1  #  初始化

        for i in range(len(s)):
            if dict[s[i]] != -1:            	
                while start <= dict[s[i]]:  # 对已有重复的reset -1 to previous ...                	
                   	dict[s[start]] = -1
                   	start += 1
            if i - start + 1 > maxlen: 
            	maxlen = i - start + 1
            dict[s[i]] = i
        return maxlen

if __name__ == '__main__':
	a = Solution()
	a.lengthOfLongestSubstring("zwxyabcabczbb")

"""
# 解法二：two pointers
# 两个指针从左往右扫描, 当头指针遇到重复字母时, 用尾指针找到上一次出现的重复字母，用此时所得子串的长度于
# 更新max, 以尾指针的index+1作为新的搜索起始位置。头指针要扫描到最后一个字母, 别忘了最后得到的子串长度
# 也要更新max。
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        maxLen = 0; subStr = '';rear = 0
        for front in range(len(s)):
            if s[front] not in subStr:
                subStr += s[front]
            else:
                maxLen = max(len(subStr),maxLen)
                while s[rear] != s[front]: # rear 会一直移动到front处
                    rear += 1
                rear += 1
                subStr = s[rear:front+1]
        return max(maxLen,len(subStr))
      

"""
# 解法二：one pointer
# The same idea as the above solution but only use one pointer
# no matter using pointers or hashtable, the idea is the same. Preferred to use substring to store sub strings. 
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subStr = ''
        ans = 0
        for char in s:
            if char not in subStr:
                subStr += char                
                ans = max(ans, len(subStr))
            else:
                cut = subStr.index(char)                
                subStr = subStr[cut+1:] + char                 
        return ans

"""
此题开始困惑我的地方是不知道如何找到新的搜索起始位置，水中的鱼解答很好
如果不以上次重复字母+1为新的搜索起始位置， 重复的字母会再次出现而且长度比以前小
"""

"""
jiuzhang solution, 可以模板化
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:return 0
        n = len(s); d = {}
        for i in range(n):
            d[s[i]] = -1
        
        i = 0; j = 0;length = 0
        for i in range(n):
            while j < n and d[s[j]] == -1:
                d[s[j]] = 1
                length = max(length, j-i+1)
                j += 1
            d[s[i]] = -1
            
        return length


















	

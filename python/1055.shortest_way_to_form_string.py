class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        s = set(source)
        t = set(target)
        for i in t:
            if i not in s:
                return -1
            
        i,j = 0,0
        res = 0
        while j < len(target):
            i = 0
            while i < len(source) and j < len(target):
                if source[i] == target[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            res += 1
        return res


遍历target的每一个字符去source字符串里找，若找完整个source字符串都没找到该字符则返回-1，否则记录下该字符在source字符串中出现的位置，找下一个字符时就从这个位置的后一个位置开始，每次把source循环一遍时把ans加一。

作者：Gaaakki
链接：https://leetcode-cn.com/problems/shortest-way-to-form-string/solution/java-by-gaaakki-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
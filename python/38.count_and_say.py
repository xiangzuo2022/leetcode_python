# A better describtion of the question: http://www.careercup.com/question?id=4425679

class Solution:
    # @param {integer} n
    # @return {string}
    def count(self,s):
    	cur = '#';count = 0; t= ''
    	for i in s:
    		if i!=cur:
    			if cur!='#':
    				t+=str(count)+cur
    			cur = i
    			count = 1
    		else:
    			count+=1
    	t+=str(count)+cur
    	return t
        
    def countAndSay(self, n):
    	s = '1'
    	for i in range(2,n+1):
    		s = self.count(s)
    	return s


    	
"""
# Solution: two pointers, prev and cur
此题完整无误的写出来还是不容易的
"""


class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
    	s = '1'
    	for i in range(0,n-1):
    		prev = newS = ''
    		num = 0
    		for cur in s:
    			if prev!='' and prev!=cur:
    				newS+=str(num)+ prev
    				num = 1
    			else:
    				num+=1
    			prev = cur
    		newS += str(num)+prev
    		s = newS
    	return s


"""
another easy-understanding solution
"""
class Solution:
    def get_next(self,s):
        length = len(s)
        num = 1
        catch = s[0] #取出第一位
        ans = ""
        for i in range(1,length):#从第二位开始比较
            if s[i] == catch: #如果与当前catch到的值相同，数量自增
                num += 1
            else:
                ans = ans + str(num) + str(catch) #如果不同，将上一个数的数量和自身追加至字符串
                catch = s[i]                      #重新取新的比较字符
                num = 1
        ans += str(num) + str(catch)              #将最后一种字符追加至字符串
        return ans



    def countAndSay(self, n: int) -> str:
        s = "1"
        for i in range(1,n):
            s = self.get_next(s)
        return s

作者：superzyc
链接：https://leetcode-cn.com/problems/count-and-say/solution/python-yi-kan-jiu-dong-fang-fa-by-superz-0t6q/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。







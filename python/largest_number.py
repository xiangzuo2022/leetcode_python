"""
# 解题思路： 排序，求解最大数，对整个列表排序，排序规则为，相邻两数组成字符串，大的靠前。
cmp：用于比较的函数，接受两个参数，根据给定的规则比较返回1（大于）,0（相等）,-1（小于），
表示第一个参数和第二个参数的大小关系; lstrip('0')表示删除最右边的零(in head)
如果希望元素能按照特定的方式进行排序（而不是sort函数默认的方式，即根据python的默认排序规则按升序排列元素），
那么可以通过compare(x,y)形式自定义比较函数。
"""


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, num):
        num = sorted([str(x) for x in num], cmp = self.compare)
        ans = ''.join(num).lstrip('0')
        return ans or '0'

    def compare(self, a, b):
    	if (a+b) > (b+a):
    		return -1
    	else:
    		return 1
        #return [1, -1][a + b > b + a]

"""
我自己的写法
"""
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        newStr = [str(i) for i in nums]
        newStr = sorted(newStr,cmp = self.compare)
        ans = int(''.join(newStr))
        return str(ans)
        
    def compare(self,a,b):
        if a+b > b + a:return -1  # 常规的是从小到大排序， 这里是从大到小排序
        else: return 1











        

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, num, target):
        num.sort()
        mindiff=100000
        res=0
        
        for i in range(len(num)):
            left=i+1; right=len(num)-1
            while left < right:
                sum=num[i]+num[left]+num[right]
                diff = abs(sum-target)
                if diff < mindiff: 
                    mindiff = diff;res=sum
                if sum==target: 
                    return sum
                elif sum < target: 
                    left+=1
                else: 
                    right-=1
        return res


# ******** The Second Time **********
"""
# 解题思路：使用一个变量mindiff来监测和与target之间的差值，如果差值为0，直接返回sum值。
# 设置左右两个指针, 用了binary search的思想
# 此方法比上面方法速度快点
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, num, target):
        num.sort()
        mindiff=100000
        res=0
        
        for i in range(len(num)):
            left=i+1; right=len(num)-1
            while left < right:
                sum=num[i]+num[left]+num[right]
                diff = abs(sum-target)
                if diff < mindiff: 
                    mindiff = diff;res=sum
                if sum==target: 
                    return sum
                elif sum < target: 
                    left+=1
                else: 
                    right-=1
        return res














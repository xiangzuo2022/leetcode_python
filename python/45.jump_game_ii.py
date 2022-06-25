class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, A):    
        ret = 0
        last = 0 # last records the maximum distance that has been reached
        curr = 0
        for i in range(len(A)):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i+A[i]) 
        return ret


#  ******** The Second Time*************
# 以下递归的做法对大数据不行，
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, A):
        lenA = len(A); maxCanReach = 0; jumpNum = 0
        if lenA == 1: return 0
        while True:
            jumpNum += 1
            for i in xrange(maxCanReach + 1):
                maxCanReach = max(maxCanReach, i + A[i])
                if maxCanReach >= lenA - 1: return jumpNum
# 题目意思是position[i]是最多能跳的距离， 也就是说可以只挑1步

"""
# Greedy, 每次jump能到达尽可能远的距离
# 要弄清各个变量的含义
# step: 到目前为止的jump数；last:进行step次jump后达到的最大距离；curr：从0~i这i+1个元素中
# 能达到得最大范围；当last < i， 说明step次jump已经不足以覆盖当前第i个元素， 因此需要增加一次jump
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        step = 0; last = 0; curr = 0
        for i in range(len(nums)):
            if last < i:
                step += 1
                last = curr
            curr = max(curr,i+nums[i]) # i + nums[i] 前面走了i次 + 当前最远能到达的距离
        return step

"""
DP time out
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        steps = []
        steps[0] = 0
        for i in range(1,len(nums)):
            steps[i] = 1<<31
            for j in range(i):
                if steps[j]!= 1<<31 and j+nums[j] >= i:
                    steps[i] = steps[j] + 1
                    break
        return steps[len(nums)-1]



























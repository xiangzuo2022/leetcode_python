"""
解法I 分治法（Divide and conquer）
递归地将表达式按照运算符拆分为左右两半
"""

def diffWaysToCompute(self, input):
    if input.isdigit():
        return [int(input)]
    res = []
    for i in xrange(len(input)):
        if input[i] in "-+*":
            res1 = self.diffWaysToCompute(input[:i])
            res2 = self.diffWaysToCompute(input[i+1:])
            for j in res1:
                for k in res2:
                    res.append(self.helper(j, k, input[i]))
    return res
    
def helper(self, m, n, op):
    if op == "+":
        return m+n
    elif op == "-":
        return m-n
    else:
        return m*n
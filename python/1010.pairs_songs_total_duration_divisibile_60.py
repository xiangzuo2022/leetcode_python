class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
    	# 字典用来统计余数及出现次数
        dic={}
        for i,t in enumerate(time):
            r = t%60
            # 若字典中没有余数 r 记录，初始化为 0
            dic.setdefault(r,0)
            dic[r]+=1
        # count 用来统计所有符合题意的组合数
        count = 0
        # 遍历 0 到 30，通过 60-i 便可拿到整除 60 后所有余数可能
        for i in range(31):
        	# 如果余数为 0  或 30，单独处理
            if i in [0,30]:
                num = dic.get(i)
                if num and num>1:
                    count+=num*(num-1)//2
            # 正常组合为 60 的余数组，取到互配的余数个数，计算结果
            else:
                num1 = dic.get(i)
                num2 = dic.get(60-i)
                if num1 and num2:                  
                    count+=num1*num2
        return count

作者：tedxpy
链接：https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/solution/bian-li-chao-shi-fen-xi-zheng-chu-60-yu-shu-ge-shu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
offical solution
"""
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0: # check if a%60==0 && b%60==0
                ret += remainders[0]
            else: # check if a%60+b%60==60
                ret += remainders[60-t%60]
            remainders[t % 60] += 1 # remember to update the remainders
        return ret
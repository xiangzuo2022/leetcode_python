"""
neighbors就是指左边一个和右边一个, 只有比neighbor的rating高的孩子得到的糖才能更多, 
rating为1, 2, 2时糖数为1, 2, 1。正向扫一遍, 后一个比前一个rating高则后一个的糖数要增加, 
再反向扫一遍, 同样处理。
"""
class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
    	n = len(ratings)
    	candy = [1 for i in range(n)]

    	for i in range(n-1):
    		if ratings[i+1] > ratings[i] and candy[i+1] < candy[i]:
    			candy[i+1] = candy[i] + 1
    	for i in reversed(n,1):
    		if ratings[i-1] > ratings[i] and candy[i-1] < candy[i]:
    			candy[i-1] = candy[i] + 1
    	return sum(candy)
   
   
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        counter = [1] * n
        for i in range(n-1):
            if ratings[i+1] > ratings[i]:
                counter[i+1] = counter[i] + 1
        
        for i in range(n-1, 0, -1):
            if ratings[i] < ratings[i-1] and counter[i-1] <= counter[i]:# the second condition is important, if it is already larger than the neighbor no need to increase the value by 1
                counter[i-1] = counter[i] + 1
        return sum(counter)
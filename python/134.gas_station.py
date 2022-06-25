class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
    	if sum(gas) < sum(cost):
    		return -1
    	diff = 0
    	index = 0    	
    	for i in range(len(gas)):
    		if gas[i] + diff < cost[i]:
    			index = i + 1
    			diff = 0
    		else:
    			diff += gas[i] - cost[i]
    	return index


# ********* The Second Time ***********
"""
# 解题思路：如果sum(gas)<sum(cost)的话，那么一定无解。
# diff是走完一站邮箱剩下的油，如果加上gas[i]也到不了下一站，那么继续将下一站设置为起点，然后再检查，
# 是不是很巧妙呢？
# 这道题挺有意思的:当diff < 0时，begin_index设为下一站的index i， 因为 i之前的station设为起点肯定
# 不能满足条件了。 这个地方我一开始想错了， 以为每次都要从上一次的fail的下一个开始。
水中的鱼的讲解很透彻
"""



class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        n = len(gas); diff = 0; begin_index = 0
        if sum(gas) < sum(cost): return -1 
        #不满足以上条件说明有解    
        for i in range(n): 
            if gas[i] + diff < cost[i]:
                begin_index = i + 1
                diff = 0  # 重置为0
            else:
                diff += gas[i] - cost[i]
        return begin_index






        
            
        

                























"""
Greedy: 先将箱子按照单元数量从大到小排序。要想卡车装载单元数最大，那么需要尽量装单元数多的箱子。所以排序以后从单元数量多的箱子开始取。
一直取至 truckSize 没有空间。累积的单元数即最大总数。
"""
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x:x[1], reverse=1)
        max_unit = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            if boxTypes[i][0] < truckSize:
                max_unit += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
                i += 1
            else:                
                max_unit += truckSize * boxTypes[i][1]
                return max_unit          
        return max_unit
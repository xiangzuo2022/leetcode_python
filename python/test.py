class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x:x[1], reverse=1)
        print(boxTypes)
        max_unit = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            if boxTypes[i][0] < truckSize:
                max_unit += boxTypes[i][0] * boxTypes[i][1]
                truckSize -= boxTypes[i][0]
                print("remaining truckSize: ",truckSize)
                i += 1
            else:
                print(truckSize, boxTypes[i][1])
                max_unit += truckSize * boxTypes[i][1]
                return max_unit          
        return max_unit

if __name__ == '__main__':
	a = Solution()
	print(a.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))











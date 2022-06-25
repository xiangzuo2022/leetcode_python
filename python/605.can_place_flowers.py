"""
greedy algorithm: 逆着考虑不能放的情况
这个题做的方式很蠢，就是一次遍历，看每个位置能不能种花，如果可以就种上，否则就判断下一个节点。
不能种花的条件是：
已经有花
当i>0时，右边有花
当i<len-1时，左边有花
注意两点：
遍历的时候如果该位置能种花，则种上，否则会影响下一个位置的判断；
最后的条件是n<=0，即能种花的位置比给出的n多。
————————————————
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/79253848
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        m = len(flowerbed)
        for i, val in enumerate(flowerbed):
            if val == 1:
                continue
            if i > 0 and flowerbed[i-1] == 1:
                continue
            if i < m -1 and flowerbed[i+1] == 1:
                continue
            flowerbed[i] = 1  # 记得要填上
            n -= 1
        return n <= 0
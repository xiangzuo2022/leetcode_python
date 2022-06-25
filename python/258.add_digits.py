class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:return num
        while num >= 10:
            carry = num / 10
            d = num % 10
            num = carry + d
        return num


"""
online solution
explonation: http://www.cnblogs.com/grandyang/p/4741028.html
"""
class Solution {
public:
    int addDigits(int num) {
        return 1 + (num - 1) % 9
    }
}
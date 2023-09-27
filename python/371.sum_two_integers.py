# https://www.youtube.com/watch?v=aDO7qhZDv10
# python cannot pass but Java code can
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0: return b
        if b == 0: return a

        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a
    
# java code
class Solution {
    public int getSum(int a, int b) {
        if (a == 0)
            return b;
        if (b == 0)
            return a;
        while (b != 0){
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
}
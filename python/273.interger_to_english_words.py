def __init__(self):
    self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    self.thousands = ["","Thousand","Million","Billion"]

def numberToWords(self, num):
    if num == 0:
        return "Zero"
    res = ""
    for i in range(len(self.thousands)):
        if num % 1000 != 0:
            res = self.helper(num%1000) + self.thousands[i] + " " + res
        num /= 1000
    return res.strip()

def helper(self, num):
    if num == 0:
        return ""
    elif num < 20:
        return self.lessThan20[num] + " "
    elif num < 100:
        return self.tens[num/10] + " " + self.helper(num%10)
    else:
        return self.lessThan20[num/100] + " Hundred " + self.helper(num%100)
    

方法一：递归
由于非负整数 
num
num 的最大值为 
2
31
−
1
2 
31
 −1，因此最多有 
10
10 位数。将整数转换成英文表示中，将数字按照 
3
3 位一组划分，将每一组的英文表示拼接之后即可得到整数 
num
num 的英文表示。

每一组最多有 
3
3 位数，可以使用递归的方式得到每一组的英文表示。根据数字所在的范围，具体做法如下：

小于 
20
20 的数可以直接得到其英文表示；

大于等于 
20
20 且小于 
100
100 的数首先将十位转换成英文表示，然后对个位递归地转换成英文表示；

大于等于 
100
100 的数首先将百位转换成英文表示，然后对其余部分（十位和个位）递归地转换成英文表示。

从高到低的每一组的单位依次是 
1
0
9
10 
9
 、
1
0
6
10 
6
 、
1
0
3
10 
3
 、
1
1，除了最低组以外，每一组都有对应的表示单位的词，分别是 
“Billion"
“Billion"、
“Million"
“Million"、
“Thousand"
“Thousand"。

得到每一组的英文表示后，需要对每一组加上对应的表示单位的词，然后拼接得到整数 
num
num 的英文表示。

具体实现中需要注意以下两点：

只有非零的组的英文表示才会拼接到整数 
num
num 的英文表示中；

如果 
num
=
0
num=0，则不适用上述做法，而是直接返回 
“Zero"
“Zero"。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/integer-to-english-words/solution/zheng-shu-zhuan-huan-ying-wen-biao-shi-b-ivik/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
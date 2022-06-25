题目大意
给出了一个字符串，其中有些字母是为了表现“情绪”而重复出现了多次，给出了一个列表，看列表中有多少个可以是这个字符串的源字符串。前提：表现语气最少需要一个字母重复三次。

解题方法
比较相同字母组的长度：
我们首先将 S 拆分成若干组相同的字母，并存储每组字母的长度。例如当 S 为 abbcccddddaaaaa 时，可以得到 5 组字母，它们分别为 abcda，长度为 [1, 2, 3, 4, 5]。

对于 words 中的每个单词 word，如果它可以扩张得到 S，那么它必须和 S 有相同的字母组。对于每一组字母，假设 S 中有 c1 个，word 中有 c2 个，那么会有下面几种情况：

如果 c1 < c2，那么 word 不能扩张得到 S；

如果 c1 >= 3，那么只要添加 c1 - c2 个字母即可；

如果 c1 < 3，由于在扩张时至少需要添加到 3 个字母，所以此时不能添加字母，必须有 c1 == c2。

如果 word 的包含的字母组中的每个字母都满足上述情况，那么 word 可以扩张得到 S。

class Solution(object):
    def expressiveWords(self, S, words):
        def RLE(S):
            return zip(*[(k, len(list(grp)))
                         for k, grp in itertools.groupby(S)])

        R, count = RLE(S)
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R: continue
            ans += all(c1 >= max(c2, 3) or c1 == c2
                       for c1, c2 in zip(count, count2))

        return ans

复杂度分析

时间复杂度：O(N + \sum k_i)O(N+∑ki )，其中 NN 是字符串 S 的长度，\sum k_i∑ki 是数组 words 中所有单词的长度之和。

空间复杂度：O(N + K)O(N+K)，其中 K 是数组 word 中最长的单词的长度。

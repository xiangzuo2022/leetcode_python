"""
一些比较巧的coding方法
思路:
首先找出在 T 中出现的所有的 S 的元素，并且将这些元素按照 S 中出现的相对顺序排序，然后把 T 中出现的但不在 S 中的元素添加到排好序的字符串中，就得到了我们想要的结果。
在将 T 中出现的但不在 S 中的元素添加到字符串时，无序关注顺序，因为这些元素并没有在 S 中出现，不需要满足排序关系。

算法:
一种巧妙的实现方法是统计 T 中每个字符出现的次数，把结果存储在数组 count 中，count[char] 表示字符 char 出现的次数。然后把在 S 中出现的字符按照在 S 中的相对顺序排列，剩余字符添加到当前字符串的后面，最终排好序的字符串顺序为 S + (未在 S 中出现的字符)。
"""
class Solution(object):
    def customSortString(self, S, T):
        # count[char] will be the number of occurrences of
        # 'char' in T.
        count = collections.Counter(T)
        ans = []

        # Write all characters that occur in S, in the order of S.
        for c in S:
            ans.append(c * count[c])
            # Set count[c] = 0 to denote that we do not need
            # to write 'c' to our answer anymore.
            count[c] = 0

        # Write all remaining characters that don't occur in S.
        # That information is specified by 'count'.
        for c in count:
            ans.append(c * count[c])

        return "".join(ans)


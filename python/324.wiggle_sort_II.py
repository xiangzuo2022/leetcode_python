"""
这道题给了我们一个无序数组，让我们排序成摆动数组，满足nums[0] < nums[1] > nums[2] < nums[3]...，并给了我们例子。我们可以先给数组排序，然后在做调整。调整的方法是找到数组的中间的数，
相当于把有序数组从中间分成两部分，然后从前半段的末尾取一个，在从后半的末尾去一个，这样保证了第一个数小于第二个数，然后从前半段取倒数第二个，从后半段取倒数第二个，这保证了第二个数大于第三个数，且第三个数小于第四个数.
O(nlogn) with O(n) extra space
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        tmp = [0]*n
        nums.sort()
        s = (n+1)/2
        t = n
        for i in range(n):
            if (i & 1) == 0:
                s -= 1
                tmp[i] = nums[s]
            else:
                t -= 1
                tmp[i] = nums[t]

        for i in range(n):
            nums[i] = tmp[i]

print(i, i&1)
(0, 0)
(1, 1)
(2, 0)
(3, 1)
(4, 0)
(5, 1)

"""
O(n)的解法很难，没有解决
"""

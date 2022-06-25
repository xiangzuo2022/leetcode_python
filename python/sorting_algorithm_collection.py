http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/

"""
Selection Sort: 不断的选择剩余元素中最小的， 找到后和第一个元素交换位置
"""


def selectionSort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j
            nums[j],nums[min_index] = nums[min_index],nums[j]
    return nums




"""
Insertion Sort: in-place排序， 需要额外空间O()
插入排序的工作原理是，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
"""
def insertSort(nums):
	for index, value in enumerate(nums):
		while index > 0 and nums[index-1] > value:
			nums[index] = nums[index-1]
			index -= 1
		nums[index] = value
	return nums


"""
Merge Sort:归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。
先考虑合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。
然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。再考虑递归分解，基本思路是将数组分
解成left和right，如果这两个数组内部数据是有序的，那么就可以用上面合并数组的方法将这两个数组合并排序。
如何让这两个数组内部是有序的？可以再二分，直至分解出的小组只含有一个元素时为止，此时认为该小组内部已有序。
然后合并排序相邻二个小组即可。
要耗费额外的空间, O(nlogn); 但在链表中得使用是不需要额外的空间的
"""

def merge_sort(nums):
	n = len(nums)
	if n <= 1: return nums
	m = n/2
	left = merge_sort(nums[:m])
	right = merge_sort(nums[m:])
	return merge(left,right)

	def merge(left,right):
		l,r = 0,0
		res = []
		while l < len(left) and r < len(right):
			if left[l] < right[r]:
				res.append(left[l])
				l += 1
			else:
				res.append(right[r])
				r += 1
		res += left[l:]
		res += right[r:]
		return res


"""
Quick Sort:快速排序通常明显比同为Ο(n log n)的其他算法更快，因此常被采用，而且快排采用了分治法的思想，
所以在很多笔试面试中能经常看到快排的影子。可见掌握快排的重要性。步骤：
1. 从数列中挑出一个元素作为基准数。
2. 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
3. 再对左右区间递归执行第二步，直至各区间只有一个数。
"""

def quick_sort(nums):
	return qsort(0,len(nums)-1)

def qsort(nums,left,right):
	if left >= right: return nums
	key = nums[left]
	lp = left; rp = right
	while lp < rp:
		while nums[rp] >= key and lp < rp:
			rp -= 1
		while nums[rp] < key and lp < rp:
			lp += 1
		nums[lp],nums[rp] = nums[rp],nums[lp]
	nums[left],nums[lp] = nums[lp],nums[left]
	qsort(nums,left,lp-1)
	qsort(nums,rp+1,right)
	return nums


"""
Heap Sort: 堆排序在 top K 问题中使用比较频繁。堆排序是采用二叉堆的数据结构来实现的，虽然实质上还是一
维数组。二叉堆是一个近似完全二叉树。 二叉堆具有以下性质：
1. 父节点的键值总是大于或等于（小于或等于）任何一个子节点的键值。
2. 每个节点的左右子树都是一个二叉堆（都是最大堆或最小堆）。
步骤：
"""

def heap_sort(ary):
	n = len(ary)
	first = int(n/2-1)
	for start in range(first,-1,-1):
		max_heapify(ary,start,n-1)
	for end in range(n-1,0,-1):
		ary[end],ary[0] = ary[0],ary[end]
		max_heapify(ary,0,end-1)
	return ary

	def max_heapify(ary,start,end):
		root = start
		while True:
			child = root*2 + 1
			if child > end: break
			if child + 1 <= end and ary[child] < ary[child+1]:
				child += 1
			if ary[root] < ary[child]:
				ary[root],ary[child] = ary[child],ary[root]
				root = child
			else: break

"""
Bucket Sort: 
"""




















































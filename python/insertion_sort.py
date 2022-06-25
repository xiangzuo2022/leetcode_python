def insertion_sort(nums):
	n = len(nums)
	for i in range(1,n):
		if nums[i] < nums[i-1]:
			tmp = nums[i]
			index = i 
			for j in range(i-1,-1,0):
				if nums[j] > tmp:
					nums[j+1] = nums[j]
					index = j
				else:
					break
			nums[index] = tmp
	return nums

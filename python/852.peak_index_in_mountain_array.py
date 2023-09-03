def peakIndexInMountainArray(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

# Example usage:
arr = [0, 1, 0]
result = peakIndexInMountainArray(arr)
print(result)  # Output: 1


# a regular binary search but needs to think about whehter the mid value will be included
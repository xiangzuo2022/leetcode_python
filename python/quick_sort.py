"""
this video is good. 
https://www.youtube.com/watch?v=CB_NCoxzQnk
this is the code:
http://www.jianshu.com/p/7ffa04799ab2
"""

def partition(nums,left,right):

    pivot_index = left; pivot = nums[left]
    for i in range(left+1, right+1):
        if nums[i] < pivot:
            pivot_index += 1
            nums[pivot_index], nums[i] = nums[i],nums[pivot_index]
    nums[left],nums[pivot_index] = nums[pivot_index],nums[left]
    return pivot_index


def quickSort(nums,left,right):

    if left < right:
        pivot_index = partition(nums,left,right)
        quickSort(nums,left,pivot_index-1)
        quickSort(nums,pivot_index+1,right)


        

if __name__ == "__main__":

    lists = [2321,232,123,1923,898,100,92]    
    quickSort(lists,0,len(lists)-1)
    print lists
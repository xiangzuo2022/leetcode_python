class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not target: return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l)//2
            print("mid=",mid)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] < nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

if __name__ == '__main__':
	a = Solution()
	print(a.search([4,5,6,7,0,1,2], 0))











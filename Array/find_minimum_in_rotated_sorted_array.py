class Solution:
    def findMin(self, nums: List[int]) -> int:
        arr_len = len(nums)
        left = 0
        right = arr_len - 1
        while(left < right):
            mid = (int)(left + ((right - left) / 2)) ## integer type and should put left for the offset
            if (nums[left] < nums[right]): return nums[left]
            elif(nums[mid] < nums[left]):
                right = mid
            else: ## should consider the case when nums[mid] == nums[left]
                left = mid + 1
        return nums[left] ## when the length of array is '1'
        
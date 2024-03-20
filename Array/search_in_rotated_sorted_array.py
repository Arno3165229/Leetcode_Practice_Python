class Solution:
    def search(self, nums: List[int], target: int) -> int:
        arr_len = len(nums)
        left = 0
        right = arr_len - 1
        while left <= right: ## should consider when the length of array is 1, so put '=' here
            mid = left + ((right - left) // 2)
            if nums[mid] == target: return mid
            if nums[mid] < nums[left]:
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid] and target >= nums[left]:
                    right = mid -1
                else:
                    left = mid + 1
            elif nums[mid] >= nums[left]: ## should consider the case when nums[mid] == nums[left]  only can put here(if-else statement) since the left will be equal to mid when the length of array is 2
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid] and target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
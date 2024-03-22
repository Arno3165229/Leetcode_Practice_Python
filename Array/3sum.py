class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr_length = len(nums)
        result = set()
        for i in range(arr_length - 2):
            j = i + 1
            k = arr_length - 1
            while j < k:
                if (nums[j] + nums[k]) == -nums[i]:
                    result.add((nums[i], nums[j], nums[k]))
                    j = j + 1
                    k = k - 1
                elif (nums[j] + nums[k]) > -nums[i]:
                    k = k - 1
                elif (nums[j] + nums[k]) < -nums[i]:
                    j = j + 1
        return result
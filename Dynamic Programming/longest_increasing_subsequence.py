class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        long_sub_array = [1] * len(nums)
        for value_index in range(1, len(nums)):
            for long_sub_array_value_index in range(0, value_index):
                if nums[value_index] > nums[long_sub_array_value_index]:
                    long_sub_array[value_index] = max(long_sub_array[value_index], long_sub_array[long_sub_array_value_index] + 1)
        return max(long_sub_array)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums), 1):
            cur_sum += nums[i]
            if nums[i] >= cur_sum:
                cur_sum = nums[i]
            max_sum = max(max_sum, cur_sum)
        return max_sum
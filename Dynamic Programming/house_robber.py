class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for dp_index in range(2, len(dp)):
            dp[dp_index] = max(dp[dp_index - 1], dp[dp_index - 2] + nums[dp_index - 1])
        return dp[-1]
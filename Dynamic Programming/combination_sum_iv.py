class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        for dp_index in range(1, len(dp)):
            for num in nums:
                if (dp_index - num) == 0:
                    dp[dp_index] += 1
                elif (dp_index - num) > 0:
                    dp[dp_index] += dp[dp_index - num]
        return dp[-1]
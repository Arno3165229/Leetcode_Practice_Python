class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ## Linear
        reachable_index = 0
        for index in range(len(nums)):
            if index > reachable_index:
                return False
            reachable_index = max(reachable_index, index + nums[index])
        return True
        
        ## DP, but time limit exceeded
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(dp)):
            for j in range(0, i):
                if dp[j] == 1 and nums[j] >= (i - j):
                    dp[i] = 1
                    break
        return dp[-1]
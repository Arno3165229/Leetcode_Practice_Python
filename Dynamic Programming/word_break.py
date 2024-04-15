class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for dp_index in range(1, len(dp)):
            for i in range(dp_index-1, -1, -1):
                if s[i:dp_index] in wordDict and dp[i] == 1:
                    dp[dp_index] = 1 
                    break
        return dp[-1]
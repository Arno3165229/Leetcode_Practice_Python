class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': ## if not s -> check if empty string
            return 0
        dp = [0] * len(s)
        dp[0] = 1

        if len(s) >= 2:
            if int(s[0:2]) <= 26 and int(s[0:2]) >= 10:
                if int(s[1]) != 0:
                    dp[1] = 2
                else:
                    dp[1] = 1
            else:
                if int(s[1]) != 0:
                    dp[1] = 1
                else:
                    dp[1] = 0

        for i in range(2, len(s)):
            if 10 <= int(s[i-1:i+1]) <= 26:
                if int(s[i]) != 0:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-2]
            else:
                if int(s[i]) != 0:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = 0
        return dp[-1]
        
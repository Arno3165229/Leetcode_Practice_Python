class Solution:
    def countSubstrings(self, s: str) -> int:
        self.totalCount = 0

        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.totalCount += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            helper(i, i)
            helper(i, i+1)
        
        return self.totalCount
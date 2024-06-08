class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cur_count = {}
        left = 0
        longest_res = 0

        for right in range(len(s)):
            cur_count[s[right]] = cur_count.get(s[right], 0) + 1

            while (right - left + 1) - max(cur_count.values()) > k:
                cur_count[s[left]] -= 1
                left += 1
            
            longest_res = max(right - left + 1, longest_res)

        return longest_res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        curr_set = set()
        longest_len = 0

        for c in s:
            while c in curr_set:
                curr_set.remove(s[left])
                left += 1
            curr_set.add(c)
            longest_len = max(right - left + 1, longest_len)
            right += 1

        return longest_len
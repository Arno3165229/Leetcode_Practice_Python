class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        long_count = 0

        for i in nums:
            cur_count = 1
            while (i - cur_count) in num_set: ## be careful of this part -> should be deducted cur_count
                cur_count += 1
            long_count = max(cur_count, long_count)
        
        return long_count

## TLE

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set (nums)
        long_count = 0

        for i in nums:
            cur_count = 0
            if i - 1 not in num_set:
                cur_count = 1
                ## Python set() is implemented using hash table, so lookup/insert/delete is O(1) for time complexity
                while i + cur_count in num_set:
                    cur_count += 1
            long_count = max(cur_count, long_count)
        
        return long_count
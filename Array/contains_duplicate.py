class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        value_count = {}
        for value in nums:
            if value in value_count and value_count[value] >= 1:
                return True
            value_count[value] = value_count.get(value, 0) + 1
        return False
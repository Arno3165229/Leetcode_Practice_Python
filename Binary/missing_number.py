class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = ((1 + len(nums)) * len(nums)) // 2
        for value in nums:
            sum = sum - value
        return sum
        ## another way is to use ^ operation 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = 1
        postfix = 1
        product_result = [0]*length
        for i in range(length):
            product_result[i] = prefix
            prefix *= nums[i]
        for i in range(length-1, -1, -1):
            product_result[i] *= postfix
            postfix *= nums[i]
        return product_result
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_cur_product = nums[0]
        max_cur_product = nums[0]
        max_product = nums[0]
        for i in range(1, len(nums), 1):
            min_cur_product *= nums[i]
            max_cur_product *= nums[i]
            temp_max_cur_product = max_cur_product ## be careful
            max_cur_product = max(max_cur_product, min_cur_product, nums[i])
            min_cur_product = min(min_cur_product, temp_max_cur_product, nums[i]) ## be careful
            max_product = max(max_product, max_cur_product)
        return max_product

class Solution:
    def maxArea(self, height: List[int]) -> int:
        array_length = len(height)
        left = 0
        right = array_length - 1
        max_area = 0
        cur_area = 0
        while left < right:
            cur_area = min(height[left], height[right]) * (right - left)
            max_area = max(cur_area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
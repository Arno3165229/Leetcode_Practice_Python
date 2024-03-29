class Solution:
    def climbStairs(self, n: int) -> int:
        total_ways = [1, 2]
        for stair in range(2, n):
            total_ways.append(total_ways[stair - 1] + total_ways[stair - 2])
        return total_ways[n - 1]
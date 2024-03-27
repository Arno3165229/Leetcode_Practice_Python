class Solution:
    def hammingWeight(self, n: int) -> int:
        number = 0
        while(n > 0):
            if (n & 1) == 1:
                number += 1
            n = n >> 1
        return number
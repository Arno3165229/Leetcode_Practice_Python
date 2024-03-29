class Solution:
    def countBits(self, n: int) -> List[int]:
        bit_num_list = [0] * (n + 1)
        for value in range(n+1):
            bit_num_list[value] = bit_num_list[value >> 1] + (value & 1) ## dp concept 
        return bit_num_list
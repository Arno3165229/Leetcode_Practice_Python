class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff 
        MAX = 0b01111111111111111111111111111111 

        if b == 0:
            return a if a <= MAX else ~(a ^ mask) 
            ## ~(a ^ mask) -> this part is kinda tricky, just to make the bits above 32 become 1. 
            ## However, when we do ~ for the whole a, the bits less than 32 will be flipped. We can use the mask to do ^ for the flipping first. 
            ## Since mask is (0b11111111.....)

        return self.getSum((a ^ b) & mask, ((a & b) << 1) & mask)
            ## the ^ xor can be seen as adding two bits but not carrying the bit
            ## so we need & and shifting for hanlding carry bit 
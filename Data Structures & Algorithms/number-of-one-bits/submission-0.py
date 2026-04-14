class Solution:
    def hammingWeight(self, n: int) -> int:
        bit_mask = 1
        count = 0
        for i in range(32):
            if n & bit_mask:
                count+=1 
            bit_mask = bit_mask << 1

        return count
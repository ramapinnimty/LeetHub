class Solution:
    def hammingWeight(self, n: int) -> int:
        # Loop till the number is reduced to 0
        num_ones = 0
        while n > 0:
            # Reduce by 1
            n &= (n-1)
            num_ones += 1

        return num_ones
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Loop till the number is reduced to 0
        num_ones = 0
        while n > 0:
            # Get the unit's digit
            num_ones += (n % 2)
            n = n>>1 # right-shift by 1

        return num_ones
# Time: O(logx) since there are ~ log_10(x) digits in `x`; Space: O(1)
class Solution:
    def reverse(self, x: int) -> int:
        # Check if `x` is -ve
        is_neg = True if x < 0 else False

        x = abs(x) # Consider the absolute value
        result = 0
        while x > 0:
            result *= 10 # move up by one place
            result += x % 10 # add the next digit

            x //= 10 # reduce `x`

        # Corner cases
        if result > 2**31 - 1 or result < -2**31:
            return 0

        return -result if is_neg else result
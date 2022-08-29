# Approach: Binary search; Time: O(logn); Space: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        '''
            Logic : 
                - sqrt(x) will ALWAYS be "less than" x / 2.
                - All we have to do is search the list 
                with squares of the already "sorted" numbers.
        '''
        # Edge case: Check if `x` is 0 or 1
        if x <= 1:
            return x

        # Iterate till we find a `nearest_square` ~ x
        start, end = 2, x // 2
        while start <= end:
            mid = start + (end - start) // 2

            # Get the nearest square
            nearest_square = mid * mid
            # Compare `x` and `nearest_square`
            if x < nearest_square:
                end = mid - 1
            elif x > nearest_square:
                start = mid + 1
            else:
                return mid

        return end
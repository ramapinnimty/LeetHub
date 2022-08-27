# Approach: Divide & Conquer; Time: O(logn); Space: O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def myPowRecrUtil(x, n):
            # Base case
            if n == 0:
                return 1

            # Throw half of the power away i.e, x^n = x^(n/2) * x^(n/2)
            result = myPowRecrUtil(x, n//2)
            result *= result # i.e, x^(n/2) * x^(n/2)

            # Deal with an "odd" power i.e, x * x^(n/2) * x^(n/2)
            return result if n % 2 == 0 else x * result

        # Kick-off recursion considering only +ve `n`
        result = myPowRecrUtil(x, abs(n))

        # Return reciprocal of the `result` if n is -ve
        return result if n >= 0 else 1 / result
# Time: O(max(|num1|, |num2|)); Space: O(max(|num1|, |num2|))
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        L1, L2 = len(num1), len(num2)
        # Initialize `carry` and `result`
        carry, result = 0, []

        # Start from the end of the strings & iterate both completely
        idx1, idx2 = L1-1, L2-1
        while idx1 >= 0 or idx2 >= 0:
            # Convert to integer while taking care of the -ve index
            x1 = ord(num1[idx1]) - ord('0') if idx1 >= 0 else 0
            x2 = ord(num2[idx2]) - ord('0') if idx2 >= 0 else 0

            # Calculate the `result` and `carry`
            result.append((x1 + x2 + carry) % 10) # Get the one's place
            carry = (x1 + x2 + carry) // 10 # Get the ten's place

            # Decrement the pointers
            idx1, idx2 = idx1-1, idx2-1
        
        # Check if there's any carry
        if carry > 0:
            result.append(carry)

        # Generate the result by reversing the list and converting `int` to `str`
        return ''.join(str(ch) for ch in result[::-1])
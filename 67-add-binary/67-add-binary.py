# Time: O(max(|a|, |b|)); Space: O(max(|a|, |b|))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
            The trick is to use carry to get the result string.
        '''
        L1, L2 = len(a), len(b)
        carry, result = 0, []

        # Start from the end of the strings & iterate through them completely
        ptr1, ptr2 = L1-1, L2-1
        while ptr1 >= 0 or ptr2 >= 0:
            # Check if we have a `1` bit in a
            if ptr1 >= 0 and a[ptr1] == '1':
                carry += 1

            # Check if we have a `1` bit in b
            if ptr2 >= 0 and b[ptr2] == '1':
                carry += 1

            # Calculate `result` and `carry`
            result.append(carry % 2)
            carry = carry // 2

            # Update pointers
            ptr1, ptr2 = ptr1-1, ptr2-1

        # Check if there's any remnant carry
        if carry == 1:
            result.append(carry)

        return ''.join(str(ch) for ch in result[::-1])
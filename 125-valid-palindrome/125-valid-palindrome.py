# Time: O(n); Space: O(n) for the updated string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase, considering only alphanumeric characters
        s = ''.join([ch for ch in s.lower() if ch.isalnum()])
        L = len(s)

        # Loop till the middle of the string
        i = 0
        while i < (L // 2):
            # Return `False` if the characters do not match
            if s[i] != s[L-1-i]:
                return False

            i += 1 # move the pointer forward

        return True # we have a palindrome!
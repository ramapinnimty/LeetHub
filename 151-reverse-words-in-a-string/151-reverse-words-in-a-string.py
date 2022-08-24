# Approach: 2-pointer; Time: O(n); Space: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        # String leading & trailing ' ' ; then split on ' '
        s = s.strip(' ').split(' ')

        # Ignore the remnant extra ' ' by considering only alphanumeric characters
        s = [word for word in s if word.isalnum()]

        start = 0
        end = len(s)-1
        # Loop till `start` crosses `end`
        while start < end:
            # Swap
            temp = s[start]
            s[start] = s[end]
            s[end] = temp

            # Update pointers
            start += 1
            end -= 1

        return ' '.join(s) # Re-join the words
# Approach: Stack ; Time: O(n); Space: O(n)
class Solution:
    def maxDepth(self, s: str) -> int:
        st = [] # stack to store '('
        maxSoFar = 0
        # Iterate through `s` considering '(' and ')'
        for ch in s:
            if ch == '(':
                st.append(ch)
                maxSoFar = max(maxSoFar, len(st)) # update current max.
            elif ch == ')':
                st.pop()

        return maxSoFar
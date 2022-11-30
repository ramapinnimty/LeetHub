# Time: O(n); Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')': '(', ']': '[', '}': '{'}
        # (1) Parse the string
        st = []
        for idx, ch in enumerate(s):
            # Push an open parenthesis onto the stack
            if ch in hmap.values():
                st.append(ch)
            # Else, I have a closing paranthesis
            else:
                # Check for the matching paranthesis at the top of the stack
                if st and st[-1] == hmap[ch]:
                    st.pop()
                else:
                    return False

        return len(st) == 0 # check if we have no remaining parentheses
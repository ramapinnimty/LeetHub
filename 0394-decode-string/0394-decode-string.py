class Solution:
    def decodeString(self, s: str) -> str:
        # Iterate through `s` and push/pop elements from the stack
        st = []
        idx = 0
        while idx < len(s):
            if s[idx] != ']':
                st.append(s[idx])
            else:
                chars = []
                while st and st[-1] != '[':
                    chars.append(st.pop())
                if st:
                    st.pop() # Pop '['
                chars.reverse()

                # Collect all the digits before '['
                digit = []
                while st and st[-1].isdigit():
                    digit.append(st.pop())
                digit.reverse() # reverse the digit since we stored in a stack
                digit = int(''.join(digit))
                st.extend(chars * digit)
            idx += 1

        return ''.join(st)
# Time: O(2n) ~ O(n); Space: O(n) for stack
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        result = []
        st = [] # each item would be [ch, continuous_frequency]
        # Iterate through all the characters in the string
        for ch in s:
            # While the string is not empty, check if the top of the stack and the incoming element are the same
            if st and st[-1][0] == ch:
                st[-1][1] += 1 # update count
                # pop the freq. list if the count is `k`
                if st[-1][1] == k:
                    st.pop()
            else:
                st.append([ch, 1]) # enter as a new, non-continuous element

        # Generate the result
        while st:
            popped_list = st.pop() # output is [ch, freq]
            ch, freq = popped_list[0], popped_list[1]
            result.extend([ch]*freq)

        return ''.join(result[::-1]) # reverse the result & return
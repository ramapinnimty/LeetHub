# Approach: 2-pointers; Time: O(n); Space: O(1)
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = len(s)

        # Reverse all the characters in the list
        s.reverse()
        # print(s)

        word_start, word_end = 0, 0
        while word_start < L and word_end < L:
            # Find the next ' ' while taking care `end` does not cross `L`
            while word_end < L and s[word_end] != ' ':
                word_end += 1 # move forward if it is not ' '
            # `end` is the location of ` `
            next_word_start = word_end + 1 # save the next word start index
            word_end -= 1 # exclude the index of ' ' for the end index of the current word

            # Swap characters at `start` and `end`
            while word_start < word_end:
                temp = s[word_start]
                s[word_start] = s[word_end]
                s[word_end] = temp

                # Update pointers
                word_start += 1
                word_end -= 1

            # Point `start` and `end` to the next word
            word_start = word_end = next_word_start